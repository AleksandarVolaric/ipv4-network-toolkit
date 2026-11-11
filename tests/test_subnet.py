import ipaddress

import pytest

from subnet import (
    broadcast_address,
    cidr_to_mask,
    first_usable_host_address,
    last_usable_host_address,
    mask_to_cidr,
    network_address,
    total_addresses,
    total_usable_addresses,
    validate_subnet_mask,
    wildcard_mask,
)


# Subnet mask conversions and validation
@pytest.mark.parametrize(
    ("prefix", "expected"),
    [
        ("0", "0.0.0.0"),
        ("24", "255.255.255.0"),
        ("27", "255.255.255.224"),
        ("32", "255.255.255.255"),
    ],
)
def test_cidr_to_mask(prefix, expected):
    assert cidr_to_mask(prefix) == expected


@pytest.mark.parametrize(
    ("mask", "expected"),
    [
        ("0.0.0.0", "0"),
        ("255.255.255.0", "24"),
        ("255.255.255.192", "26"),
        ("255.255.255.255", "32"),
    ],
)
def test_mask_to_cidr(mask, expected):
    assert validate_subnet_mask(mask) is None
    assert mask_to_cidr(mask) == expected


@pytest.mark.parametrize(
    "mask",
    [
        "255.255.255",
        "255.255.255.255.0",
        "255.255.256.0",
        "255.255.one.0",
        "255.0.255.0",
    ],
)
def test_invalid_subnet_mask(mask):
    assert validate_subnet_mask(mask) is not None


# Network, broadcast, and usable-host calculations
@pytest.mark.parametrize(
    ("address", "prefix", "expected"),
    [
        ("192.168.10.34", 27, "192.168.10.32"),
        ("10.0.0.1", 8, "10.0.0.0"),
        ("172.16.0.1", 12, "172.16.0.0"),
    ],
)
def test_network_address(address, prefix, expected):
    assert network_address(address, prefix) == expected


@pytest.mark.parametrize(
    ("address", "prefix", "expected"),
    [
        ("192.168.10.34", 27, "192.168.10.63"),
        ("10.0.0.1", 8, "10.255.255.255"),
        ("172.16.0.1", 12, "172.31.255.255"),
    ],
)
def test_broadcast_address(address, prefix, expected):
    assert broadcast_address(address, prefix) == expected


@pytest.mark.parametrize(
    ("network", "prefix", "expected"),
    [
        ("192.168.10.32", 27, "192.168.10.33"),
        ("10.0.0.255", 8, "10.0.1.0"),
        ("192.0.2.0", 31, "192.0.2.0"),
        ("192.0.2.5", 32, "192.0.2.5"),
    ],
)
def test_first_usable_host_address(network, prefix, expected):
    assert first_usable_host_address(network, prefix) == expected


@pytest.mark.parametrize(
    ("broadcast", "prefix", "expected"),
    [
        ("192.168.10.63", 27, "192.168.10.62"),
        ("10.0.1.0", 8, "10.0.0.255"),
        ("192.0.2.1", 31, "192.0.2.1"),
        ("192.0.2.5", 32, "192.0.2.5"),
    ],
)
def test_last_usable_host_address(broadcast, prefix, expected):
    assert last_usable_host_address(broadcast, prefix) == expected


@pytest.mark.parametrize(
    ("prefix", "expected"),
    [
        (0, 4294967296),
        (27, 32),
        (32, 1),
    ],
)
def test_total_addresses(prefix, expected):
    assert total_addresses(prefix) == expected


@pytest.mark.parametrize(
    ("prefix", "expected"),
    [
        (0, 4294967294),
        (27, 30),
        (30, 2),
        (31, 2),
        (32, 1),
    ],
)
def test_total_usable_addresses(prefix, expected):
    assert total_usable_addresses(prefix) == expected


# Wildcard mask calculation
@pytest.mark.parametrize(
    ("prefix", "expected"),
    [
        (0, "255.255.255.255"),
        (27, "0.0.0.31"),
        (32, "0.0.0.0"),
    ],
)
def test_wildcard_mask(prefix, expected):
    assert wildcard_mask(prefix) == expected



# Compare the project calculations with Python's standard-library reference.
@pytest.mark.parametrize(
    ("address", "prefix"),
    [
        ("10.0.0.1", 8),
        ("172.16.10.50", 12),
        ("192.168.1.1", 24),
        ("192.168.10.34", 27),
        ("192.168.1.1", 30),
        ("192.0.2.0", 31),
        ("192.0.2.5", 32),
        ("0.0.0.0", 0),
    ],
)
def test_subnet_calculations_match_ipaddress(address, prefix):
    """Check subnet results against ipaddress, including the project's /31 and /32 rules."""
    reference_network = ipaddress.ip_network(f"{address}/{prefix}", strict=False)
    network = str(reference_network.network_address)
    broadcast = str(reference_network.broadcast_address)

    assert network_address(address, prefix) == network
    assert broadcast_address(address, prefix) == broadcast
    assert total_addresses(prefix) == reference_network.num_addresses

    first_reference_host = str(next(reference_network.hosts()))
    assert first_usable_host_address(network, prefix) == first_reference_host

    if prefix <= 30:
        last_reference_host = str(reference_network.broadcast_address - 1)
        expected_usable_hosts = reference_network.num_addresses - 2
    else:
        last_reference_host = broadcast
        expected_usable_hosts = reference_network.num_addresses

    assert last_usable_host_address(broadcast, prefix) == last_reference_host
    assert total_usable_addresses(prefix) == expected_usable_hosts

import pytest

from ipv4 import (
    ipv4_to_bin,
    ipv4_to_dec,
    validate_binary_ipv4,
    validate_cidr,
    classify_ipv4_address,
)

from main import main

from subnet import (
    cidr_to_mask,
    mask_to_cidr,
    validate_subnet_mask,
    network_address,
    broadcast_address,
    first_usable_host_address,
    last_usable_host_address,
    total_addresses,
    total_usable_addresses,
    wildcard_mask,
)


@pytest.mark.parametrize(
    "user_input",
    [
        "192.168.1.1/24",
        "192.168.10.34/27",
        "0.0.0.0/0",
        "255.255.255.255/32",
    ],
)
def test_valid_cidr(user_input):
    assert validate_cidr(user_input) is None


@pytest.mark.parametrize(
    "user_input",
    [
        "192.168.1.256/24",
        "192.168.1.-1/24",
        "192.168.one.1/24",
        "192.168.1/24",
        "192.168.1.1.5/24",
        "192.168.1.1/33",
        "192.168.1.1/-1",
        "192.168.1.1/hello",
        "192.168.1.1/",
        "192.168.1.1/24/5",
    ],
)
def test_invalid_cidr(user_input):
    assert validate_cidr(user_input) is not None


@pytest.mark.parametrize(
    ("address", "expected"),
    [
        ("192.168.10.34", "11000000.10101000.00001010.00100010"),
        ("0.0.0.0", "00000000.00000000.00000000.00000000"),
        ("255.255.255.255", "11111111.11111111.11111111.11111111"),
    ],
)
def test_ipv4_to_bin(address, expected):
    assert ipv4_to_bin(address) == expected


@pytest.mark.parametrize(
    ("binary_address", "expected"),
    [
        ("11000000.10101000.00001010.00100010", "192.168.10.34"),
        ("00000000.00000000.00000000.00000000", "0.0.0.0"),
        ("11111111.11111111.11111111.11111111", "255.255.255.255"),
    ],
)
def test_ipv4_to_dec(binary_address, expected):
    assert ipv4_to_dec(binary_address) == expected


@pytest.mark.parametrize(
    "binary_address",
    [
        "11000000.10101000.00001010",
        "11000000.10101000.00001010.00100010.00000000",
        "11000000.10101000.00001010.0010001",
        "11000000.10101000.00001010.00100012",
    ],
)
def test_invalid_binary_ipv4(binary_address):
    assert validate_binary_ipv4(binary_address) is not None


def test_valid_binary_ipv4():
    assert validate_binary_ipv4(
        "11000000.10101000.00001010.00100010"
    ) is None


@pytest.mark.parametrize(
    ("address", "expected"),
    [
        ("0.0.0.0", "Unspecified"),
        ("255.255.255.255", "Limited broadcast"),
        ("127.0.0.0", "Loopback"),
        ("127.255.255.255", "Loopback"),
        ("126.255.255.255", "Public"),
        ("128.0.0.0", "Public"),
        ("169.254.0.0", "Link-local"),
        ("169.254.255.255", "Link-local"),
        ("169.253.255.255", "Public"),
        ("169.255.0.0", "Public"),
        ("10.0.0.0", "Private"),
        ("10.255.255.255", "Private"),
        ("9.255.255.255", "Public"),
        ("11.0.0.0", "Public"),
        ("172.16.0.0", "Private"),
        ("172.31.255.255", "Private"),
        ("172.15.255.255", "Public"),
        ("172.32.0.0", "Public"),
        ("192.168.0.0", "Private"),
        ("192.168.255.255", "Private"),
        ("192.167.255.255", "Public"),
        ("192.169.0.0", "Public"),
        ("224.0.0.0", "Multicast"),
        ("239.255.255.255", "Multicast"),
        ("223.255.255.255", "Public"),
        ("240.0.0.0", "Public"),
        ("8.8.8.8", "Public"),
    ],
)
def test_classify_ipv4_address(address, expected):
    assert classify_ipv4_address(address) == expected


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


def test_cli_analysis_returns_to_menu(monkeypatch, capsys):
    user_inputs = iter(["1", "192.168.10.34/27", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(user_inputs))

    main()

    output = capsys.readouterr().out
    assert "IPv4 address: 192.168.10.34" in output
    assert "Wildcard mask: 0.0.0.31" in output
    assert "Network address: 192.168.10.32" in output
    assert "IPv4 classification: Private" in output
    assert output.count("1. Analyze IPv4 network") == 2
    assert "Goodbye!" in output


def test_cli_invalid_cidr_returns_to_menu(monkeypatch, capsys):
    user_inputs = iter(["1", "192.168.10.999/27", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(user_inputs))

    main()

    output = capsys.readouterr().out
    assert "Invalid octet: 999." in output
    assert output.count("1. Analyze IPv4 network") == 2


def test_cli_conversion_returns_to_menu(monkeypatch, capsys):
    user_inputs = iter(["2", "192.168.10.34", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(user_inputs))

    main()

    output = capsys.readouterr().out
    assert "Binary address: 11000000.10101000.00001010.00100010" in output
    assert output.count("1. Analyze IPv4 network") == 2
    assert "Goodbye!" in output
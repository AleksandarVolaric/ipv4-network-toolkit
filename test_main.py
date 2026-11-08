import pytest

from main import (ipv4_to_bin, ipv4_to_dec, validate_binary_ipv4, validate_cidr)


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

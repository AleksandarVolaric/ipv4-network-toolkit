# IPv4 Network Toolkit

A small command-line project for validating IPv4/CIDR input and converting IPv4 addresses between decimal and binary.

**Current version:** 0.2.0

## Implemented features

- Accepts an IPv4 address with a CIDR prefix, such as `192.168.10.34/27`.
- Checks that the address has exactly four octets and each is between 0 and 255.
- Checks that the prefix is a number from 0 to 32.
- Converts a valid decimal IPv4 address to four 8-bit binary octets.
- Validates binary IPv4 input: four octets, each exactly eight bits containing only `0` and `1`.
- Converts valid binary IPv4 input back to decimal.
- Includes pytest tests for validation and conversions.

This version does not calculate network or host details.

## Examples

Valid input:

```text
192.168.10.34/27
```

The program displays its binary form:

```text
11000000.10101000.00001010.00100010
```

For binary-to-decimal conversion, enter:

```text
11000000.10101000.00001010.00100010
```

The program displays `192.168.10.34`.

Invalid input:

```text
192.168.1.256/24
```

The program reports that the octet must be between 0 and 255. Binary input is also checked; each octet must be eight `0` or `1` characters.

## Run the program

From the project directory, run:

```text
python main.py
```

Enter an IPv4 address and prefix when prompted. Then enter a binary IPv4 address when prompted for the reverse conversion.

## Run the tests

Install pytest if needed, then run:

```text
python -m pytest
```

## Project structure

```text
.
├── main.py       # Validation, conversions, and command-line input/output
├── test_main.py  # Tests for validation and conversions
└── README.md
```

## Planned future features

These are not implemented in version 0.2.0:

- CIDR to subnet mask conversion
- Subnet mask to CIDR conversion
- Network and broadcast address calculation
- First and last usable host calculation
- Usable host count
- Private/public IPv4 detection

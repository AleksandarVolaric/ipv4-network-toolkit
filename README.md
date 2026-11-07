# IPv4 Network Toolkit

A small command-line project for checking whether an IPv4 address and CIDR prefix are valid.

**Current version:** 0.1.0

## Implemented features

- Accepts an IPv4 address with a CIDR prefix, such as `192.168.10.34/27`.
- Checks that the address has exactly four octets and each is between 0 and 255.
- Checks that the prefix is a number from 0 to 32.
- Prints a success message for valid input or an error message for invalid input.
- Includes pytest tests for valid and invalid input.

This version validates input only. It does not calculate network or host details.

## Examples

Valid input:

```text
192.168.10.34/27
```

The program reports that the IPv4 address and prefix are valid.

Invalid input:

```text
192.168.1.256/24
```

The program reports that the octet must be between 0 and 255.

## Run the program

From the project directory, run:

```text
python main.py
```

Enter an IPv4 address and prefix when prompted.

## Run the tests

Install pytest if needed, then run:

```text
python -m pytest
```

## Project structure

```text
.
├── main.py       # CIDR validation and command-line input/output
├── test_main.py  # Tests for valid and invalid CIDR input
└── README.md
```

## Planned future features

These are not implemented in version 0.1.0:

- Decimal IPv4 to binary conversion
- Binary IPv4 to decimal conversion
- CIDR to subnet mask conversion
- Subnet mask to CIDR conversion
- Network and broadcast address calculation
- First and last usable host calculation
- Usable host count
- Private/public IPv4 detection

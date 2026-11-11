# IPv4 Network Toolkit

A beginner project for exploring IPv4 addresses, CIDR prefixes, and subnet calculations through a command-line menu or a simple graphical interface.

**Current stable version:** 1.0.0

## Motivation

This project was built as a learning and portfolio project after CS50P. It provides a way to practice Python by implementing IPv4 validation and subnet calculations, then using those functions from both a CLI and a GUI.

## Features

- Validates IPv4 addresses, CIDR prefixes, binary IPv4 addresses, and subnet masks.
- Converts decimal IPv4 addresses to binary and binary addresses back to decimal.
- Converts between CIDR prefixes and subnet masks.
- Calculates wildcard masks, network addresses, and broadcast addresses.
- Calculates first and last usable host addresses, total addresses, and usable hosts.
- Classifies addresses as private, public, loopback, link-local, multicast, unspecified, or limited broadcast.
- Provides a menu-driven command-line interface and a basic Tkinter GUI.
- Uses the same calculation and validation functions for both interfaces.
- Includes pytest tests for the functions, CLI behavior, and selected subnet comparisons with Python's standard-library `ipaddress` module.

## Example

For `192.168.10.34/27`, network analysis displays:

```text
IPv4 address: 192.168.10.34
CIDR prefix: /27
Binary address: 11000000.10101000.00001010.00100010
Subnet mask: 255.255.255.224
Wildcard mask: 0.0.0.31
Network address: 192.168.10.32
Broadcast address: 192.168.10.63
First usable host: 192.168.10.33
Last usable host: 192.168.10.62
Total addresses: 32
Usable hosts: 30
IPv4 classification: Private
```

## Run the command-line interface

From the project directory, run:

```text
python main.py
```

Choose an operation from the menu. The CLI asks only for the input relevant to that operation and returns to the menu when it finishes.

## Run the graphical interface

From the project directory, run:

```text
python gui.py
```

Enter an IPv4 address with a CIDR prefix and select **Analyze** to see subnet details. The GUI also has separate conversion tools for decimal/binary IPv4 addresses and CIDR/subnet masks.

Both interfaces call the same functions in `ipv4.py` and `subnet.py`. The user interfaces collect input and display results; they do not implement separate networking calculations.

## Run the tests

Install pytest if needed, then run from the project directory:

```text
python -m pytest
```

The application uses Python and the standard-library Tkinter GUI toolkit. Tests use pytest and Python's standard-library `ipaddress` module for selected verification comparisons.

## Project structure

```text
.
├── main.py             # Command-line menu
├── gui.py              # Tkinter graphical interface
├── ipv4.py             # IPv4 validation, conversion, and classification
├── subnet.py           # Subnet validation and calculations
├── tests/
│   ├── test_ipv4.py    # IPv4 validation, conversions, and classification
│   ├── test_subnet.py  # Subnet validation and calculations
│   └── test_cli.py     # CLI menu behavior
├── CHANGELOG.md        # Development history
└── README.md
```

## Technical overview

The reusable validation and IPv4 functions are in `ipv4.py`; subnet-mask and subnet calculations are in `subnet.py`. The CLI and GUI import those functions and use them to process user input. The `ipaddress` module is only used in tests as a reference for selected subnet results.

## Known limitations

- The GUI is intentionally basic and is meant for learning, not as a polished application.
- Address classification follows the project's listed categories; addresses outside them are labeled public, which is a simplified rule and does not guarantee global reachability.
- Usable-host counts use the project's stated conventions: `/31` has two usable addresses and `/32` has one.
- There is no language-selection feature.

See [CHANGELOG.md](./CHANGELOG.md) for the version history.

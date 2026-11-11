# IPv4 Network Toolkit

A beginner IPv4 toolkit with a command-line menu and a simple Tkinter GUI. Both interfaces use the same validation, conversion, subnet calculation, and classification functions.

**Current version:** 0.7.0

## Implemented features

- Validates an IPv4 address with a CIDR prefix, such as `192.168.10.34/27`.
- Checks for four decimal octets in the range 0-255 and a prefix in the range 0-32.
- Converts a decimal IPv4 address to four 8-bit binary octets.
- Validates binary IPv4 input and converts it back to decimal.
- Converts a CIDR prefix to a subnet mask, such as `/27` to `255.255.255.224`.
- Validates subnet masks, including that their 1 bits are continuous before their 0 bits.
- Converts a valid subnet mask to its CIDR prefix, such as `255.255.255.192` to `/26`.
- Calculates network and broadcast addresses.
- Calculates the wildcard mask from a CIDR prefix.
- Calculates first and last usable host addresses.
- Calculates the total number of addresses and usable addresses in a subnet.
- Handles `/31` subnets as having two usable addresses and `/32` subnets as having one.
- Classifies IPv4 addresses as private, public, loopback, link-local, multicast, unspecified, or limited broadcast.
- Provides a CLI menu for network analysis and standalone conversions.
- Provides a basic Tkinter GUI for network analysis and standalone conversions.
- Includes pytest tests organized by IPv4 functionality, subnet calculations, and CLI behavior.
- Uses Python's standard-library `ipaddress` module in selected tests to verify subnet calculation results.

## Example

For the input `192.168.10.34/27`, the program displays:

```text
Binary address: 11000000.10101000.00001010.00100010
IPv4 classification: Private
Subnet mask: 255.255.255.224
Wildcard mask: 0.0.0.31
Network address: 192.168.10.32
Broadcast address: 192.168.10.63
First usable host: 192.168.10.33
Last usable host: 192.168.10.62
Total addresses: 32
Total usable addresses: 30
```

After analysis, the CLI returns to its menu. The standalone conversion options can be selected separately. For example, converting this binary address:

```text
11000000.10101000.00001010.00100010
255.255.255.192
```

The corresponding decimal address and CIDR prefix are:

```text
192.168.10.34
/26
```

Invalid input produces an error message. For example, `255.0.255.0` is rejected as a subnet mask because its 1 bits are not continuous.

## Run the command-line interface

From the project directory, run:

```text
python main.py
```

Choose an operation from the menu. The CLI asks only for input relevant to that operation and returns to the menu when it finishes.

## Run the graphical interface

From the project directory, run:

```text
python gui.py
```

Enter an IPv4 address with a CIDR prefix and select **Analyze** to see subnet details. The GUI also provides separate fields for decimal-to-binary, binary-to-decimal, CIDR-to-mask, and mask-to-CIDR conversions. Both the CLI and GUI call the same functions in `ipv4.py` and `subnet.py`; their input and display code does not perform its own networking calculations.

## Run the tests

Install pytest if needed, then run:

```text
python -m pytest
```

## Project structure

```text
.
├── main.py       # Command-line menu and output
├── gui.py        # Tkinter graphical interface
├── ipv4.py       # IPv4/CIDR validation and decimal/binary conversions
├── subnet.py     # Subnet-mask validation and subnet calculations
├── tests/
│   ├── test_ipv4.py  # IPv4 validation, conversions, and classification
│   ├── test_subnet.py  # Subnet validation and calculations
│   └── test_cli.py  # CLI menu behavior
├── CHANGELOG.md  # Notes on changes by version
└── README.md
```

## Current limitations

The GUI is intentionally basic and is intended as a learning interface. The toolkit does not currently provide a menu for choosing a language.

Some subnet and host-count conventions for `/31` and `/32` are project assumptions documented by tests; `ipaddress` is used only to verify selected network calculations, not by the application itself.

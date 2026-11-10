# IPv4 Network Toolkit

A beginner command-line project for validating and converting IPv4 addresses, calculating subnet details, and classifying IPv4 addresses.

**Current version:** 0.5.0

## Implemented features

- Validates an IPv4 address with a CIDR prefix, such as `192.168.10.34/27`.
- Checks for four decimal octets in the range 0-255 and a prefix in the range 0-32.
- Converts a decimal IPv4 address to four 8-bit binary octets.
- Validates binary IPv4 input and converts it back to decimal.
- Converts a CIDR prefix to a subnet mask, such as `/27` to `255.255.255.224`.
- Validates subnet masks, including that their 1 bits are continuous before their 0 bits.
- Converts a valid subnet mask to its CIDR prefix, such as `255.255.255.192` to `/26`.
- Calculates network and broadcast addresses.
- Calculates first and last usable host addresses.
- Calculates the total number of addresses and usable addresses in a subnet.
- Handles `/31` subnets as having two usable addresses and `/32` subnets as having one.
- Classifies IPv4 addresses as private, public, loopback, link-local, multicast, unspecified, or limited broadcast.
- Includes pytest tests for validation, conversions, calculations, and classification.

The command-line program asks for each supported input in sequence and does not provide a menu.

## Example

For the input `192.168.10.34/27`, the program displays:

```text
Binary address: 11000000.10101000.00001010.00100010
IPv4 classification: Private
Subnet mask: 255.255.255.224
Network address: 192.168.10.32
Broadcast address: 192.168.10.63
First usable host: 192.168.10.33
Last usable host: 192.168.10.62
Total addresses: 32
Total usable addresses: 30
```

It then asks for a binary IPv4 address and a subnet mask to convert. For example:

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

## Run the program

From the project directory, run:

```text
python main.py
```

Follow the prompts to enter a decimal IPv4 address with prefix, a binary IPv4 address, and a subnet mask.

## Run the tests

Install pytest if needed, then run:

```text
python -m pytest
```

## Project structure

```text
.
├── main.py       # Command-line prompts and output
├── ipv4.py       # IPv4/CIDR validation and decimal/binary conversions
├── subnet.py     # Subnet-mask validation and CIDR/mask conversions
├── test_main.py  # Tests for validation and conversions
├── CHANGELOG.md  # Notes on changes by version
└── README.md
```

## Planned future features

These are not implemented in version 0.5.0:

- A menu for choosing which operation to run

# Changelog

Notable project changes are recorded here.

## 0.4.0

- Added network and broadcast address calculations.
- Added first and last usable host address calculations.
- Added total and usable address counts, including `/31` and `/32` handling.
- Updated the command-line output, tests, and documentation for subnet calculations.

## 0.3.0

- Added CIDR prefix-to-subnet-mask conversion.
- Added subnet-mask validation and subnet-mask-to-CIDR conversion.
- Split reusable IPv4 and subnet functions into `ipv4.py` and `subnet.py`.
- Updated tests and documentation for the new structure and features.

## 0.2.0

- Added decimal IPv4-to-binary conversion.
- Added validation and binary IPv4-to-decimal conversion.
- Added tests for the conversion features.

## 0.1.0

- Added IPv4 address and CIDR prefix validation.
- Added tests for valid and invalid CIDR input.

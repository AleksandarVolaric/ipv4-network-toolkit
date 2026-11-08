from ipv4 import (ipv4_to_bin, ipv4_to_dec, validate_binary_ipv4, validate_cidr)
from subnet import cidr_to_mask, mask_to_cidr, validate_subnet_mask


def main():
    user_input = input("Enter an IPv4 address with prefix (example: 192.168.10.34/27): ")
    error = validate_cidr(user_input)

    if error is None:
        address, prefix = user_input.split("/")
        print(f"Binary address: {ipv4_to_bin(address)}")
        print(f"Subnet mask: {cidr_to_mask(prefix)}")

        binary_address = input("Enter a binary IPv4 address: ")
        error = validate_binary_ipv4(binary_address)

        if error is None:
            print(f"Decimal address: {ipv4_to_dec(binary_address)}")
        else:
            print(error)

        subnet_mask = input("Enter a subnet mask to convert to CIDR: ")
        error = validate_subnet_mask(subnet_mask)

        if error is None:
            print(f"CIDR prefix: /{mask_to_cidr(subnet_mask)}")
        else:
            print(error)
    else:
        print(error)



if __name__ == "__main__":
    main()

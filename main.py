from ipv4 import (
    ipv4_to_bin,
    ipv4_to_dec,
    validate_binary_ipv4,
    validate_cidr,
    classify_ipv4_address,
)

from subnet import (
    broadcast_address,
    cidr_to_mask,
    mask_to_cidr,
    network_address,
    validate_subnet_mask,
    first_usable_host_address,
    last_usable_host_address,
    total_addresses,
    total_usable_addresses,
)


def main():
    user_input = input("Enter an IPv4 address with prefix (example: 192.168.10.34/27): ")
    error = validate_cidr(user_input)

    if error is None:
        address, prefix = user_input.split("/")
        print(f"Binary address: {ipv4_to_bin(address)}")
        print(f"IPv4 classification: {classify_ipv4_address(address)}")
        print(f"Subnet mask: {cidr_to_mask(prefix)}")
        network = network_address(address, prefix)
        broadcast = broadcast_address(address, prefix)
        print(f"Network address: {network}")
        print(f"Broadcast address: {broadcast}")
        print(f"First usable host: {first_usable_host_address(network, prefix)}")
        print(f"Last usable host: {last_usable_host_address(broadcast, prefix)}")
        print(f"Total addresses: {total_addresses(prefix)}")
        print(f"Total usable addresses: {total_usable_addresses(prefix)}")

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
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
    wildcard_mask,
)


def show_network_analysis(user_input):
    error = validate_cidr(user_input)
    if error is not None:
        print(error)
        return

    address, prefix = user_input.split("/")
    network = network_address(address, prefix)
    broadcast = broadcast_address(address, prefix)

    print(f"IPv4 address: {address}")
    print(f"CIDR prefix: /{prefix}")
    print(f"Binary address: {ipv4_to_bin(address)}")
    print(f"Subnet mask: {cidr_to_mask(prefix)}")
    print(f"Wildcard mask: {wildcard_mask(prefix)}")
    print(f"Network address: {network}")
    print(f"Broadcast address: {broadcast}")
    print(f"First usable host: {first_usable_host_address(network, prefix)}")
    print(f"Last usable host: {last_usable_host_address(broadcast, prefix)}")
    print(f"Total addresses: {total_addresses(prefix)}")
    print(f"Usable hosts: {total_usable_addresses(prefix)}")
    print(f"IPv4 classification: {classify_ipv4_address(address)}")


def main():
    while True:
        print("\nIPv4 Network Toolkit")
        print("1. Analyze IPv4 network")
        print("2. Decimal IPv4 to Binary")
        print("3. Binary IPv4 to Decimal")
        print("4. CIDR to Subnet Mask")
        print("5. Subnet Mask to CIDR")
        print("6. Classify IPv4 Address")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            user_input = input("Enter an IPv4 address with prefix (example: 192.168.10.34/27): ").strip()
            show_network_analysis(user_input)
        elif choice == "2":
            address = input("Enter a decimal IPv4 address: ").strip()
            error = validate_cidr(f"{address}/32")
            if error is None:
                print(f"Binary address: {ipv4_to_bin(address)}")
            else:
                print(error)
        elif choice == "3":
            binary_address = input("Enter a binary IPv4 address: ").strip()
            error = validate_binary_ipv4(binary_address)
            if error is None:
                print(f"Decimal address: {ipv4_to_dec(binary_address)}")
            else:
                print(error)
        elif choice == "4":
            prefix = input("Enter a CIDR prefix (0-32): ").strip()
            error = validate_cidr(f"0.0.0.0/{prefix}")
            if error is None:
                print(f"Subnet mask: {cidr_to_mask(prefix)}")
            else:
                print(error)
        elif choice == "5":
            subnet_mask = input("Enter a subnet mask: ").strip()
            error = validate_subnet_mask(subnet_mask)
            if error is None:
                print(f"CIDR prefix: /{mask_to_cidr(subnet_mask)}")
            else:
                print(error)
        elif choice == "6":
            address = input("Enter a decimal IPv4 address: ").strip()
            error = validate_cidr(f"{address}/32")
            if error is None:
                print(f"IPv4 classification: {classify_ipv4_address(address)}")
            else:
                print(error)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
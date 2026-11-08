def validate_cidr(user_input):
    parts = user_input.strip().split("/")

    if len(parts) != 2:
        return "Enter an IPv4 address followed by one prefix, separated by '/'."

    address = parts[0]
    prefix = parts[1]
    octets = address.split(".")

    if len(octets) != 4:
        return "An IPv4 address must have exactly four octets."

    for octet in octets:
        if not octet.isdigit():
            return f"Invalid octet: {octet}. Each octet must be a number from 0 to 255."

        if not 0 <= int(octet) <= 255:
            return f"Invalid octet: {octet}. Each octet must be a number from 0 to 255."

    if not prefix.isdigit():
        return "Invalid prefix length. It must be a number from 0 to 32."

    if not 0 <= int(prefix) <= 32:
        return "Invalid prefix length. It must be a number from 0 to 32."

    return None


def validate_binary_ipv4(binary_address):
    octets = binary_address.split(".")

    if len(octets) != 4:
        return "A binary IPv4 address must have exactly four octets."

    for octet in octets:
        if len(octet) != 8:
            return "Each binary octet must contain exactly eight bits."

        for bit in octet:
            if bit != "0" and bit != "1":
                return "Binary octets can contain only 0 and 1."

    return None




def dec_to_bin(octet):
    return format(int(octet), "08b")

def ipv4_to_bin(address):
    octets = address.split(".")
    binary_octets = [dec_to_bin(octet) for octet in octets]
    return ".".join(binary_octets)




def bin_to_dec(binary_octet):
    return str(int(binary_octet, 2))

def ipv4_to_dec(binary_address):
    binary_octets = binary_address.split(".")
    decimal_octets = [bin_to_dec(octet) for octet in binary_octets]
    return ".".join(decimal_octets)




def main():
    user_input = input("Enter an IPv4 address with prefix (example: 192.168.10.34/27): ")
    error = validate_cidr(user_input)

    if error is None:
        address = user_input.split("/")[0]
        print(f"Binary address: {ipv4_to_bin(address)}")

        binary_address = input("Enter a binary IPv4 address: ")
        error = validate_binary_ipv4(binary_address)

        if error is None:
            print(f"Decimal address: {ipv4_to_dec(binary_address)}")
        else:
            print(error)
    else:
        print(error)



if __name__ == "__main__":
    main()
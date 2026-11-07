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


def main():
    user_input = input("Enter an IPv4 address with prefix (example: 192.168.10.34/27): ")
    error = validate_cidr(user_input)

    if error is None:
        print("The IPv4 address and prefix are valid.")
    else:
        print(error)


if __name__ == "__main__":
    main()
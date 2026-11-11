def validate_cidr(user_input):
    """Return an error message if the IPv4/CIDR input is invalid, otherwise None."""
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
    """Return an error message if the binary IPv4 address is invalid, otherwise None."""
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
    """Convert one decimal IPv4 octet to an 8-bit binary string."""
    return format(int(octet), "08b")


def ipv4_to_bin(address):
    """Convert a dotted-decimal IPv4 address to four binary octets."""
    octets = address.split(".")
    binary_octets = [dec_to_bin(octet) for octet in octets]
    return ".".join(binary_octets)



def bin_to_dec(binary_octet):
    """Convert one 8-bit binary octet to a decimal string."""
    return str(int(binary_octet, 2))


def ipv4_to_dec(binary_address):
    """Convert four binary IPv4 octets to a dotted-decimal address."""
    binary_octets = binary_address.split(".")
    decimal_octets = [bin_to_dec(octet) for octet in binary_octets]
    return ".".join(decimal_octets)


def classify_ipv4_address(address):
    """Return the toolkit's classification for a validated IPv4 address."""
    octets = [int(octet) for octet in address.split(".")]
    if address == "0.0.0.0":
        return "Unspecified"
    elif address == "255.255.255.255":
        return "Limited broadcast"
    elif octets[0] == 127:
        return "Loopback"
    elif octets[0] == 169 and octets [1] == 254:
        return "Link-local"
    elif octets[0] == 10:
        return "Private"
    elif octets[0] == 172 and 16 <= octets[1] <= 31:
        return "Private"
    elif octets[0] == 192 and octets[1] == 168:
        return "Private"
    elif 224 <= octets[0] <= 239:
        return "Multicast"
    else:
        return "Public"
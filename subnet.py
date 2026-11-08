from ipv4 import bin_to_dec, dec_to_bin


def validate_subnet_mask(mask):
    octets = mask.split(".")

    if len(octets) != 4:
        return "A subnet mask must have exactly four octets."

    for octet in octets:
        if not octet.isdigit():
            return f"Invalid subnet mask octet: {octet}."

        if not 0 <= int(octet) <= 255:
            return f"Invalid subnet mask octet: {octet}. It must be from 0 to 255."

    binary_mask = "".join(dec_to_bin(octet) for octet in octets)

    if "01" in binary_mask:
        return "Subnet mask bits must be continuous: 1 bits followed by 0 bits."

    return None



def cidr_to_mask(prefix):
    prefix = int(prefix)
    binary_mask = "1" * prefix + "0" * (32 - prefix)
    octets = [
        binary_mask[0:8],
        binary_mask[8:16],
        binary_mask[16:24],
        binary_mask[24:32],
    ]
    decimal_octets = [bin_to_dec(octet) for octet in octets]
    return ".".join(decimal_octets)


def mask_to_cidr(mask):
    octets = mask.split(".")
    binary_mask = "".join(dec_to_bin(octet) for octet in octets)
    return str(binary_mask.count("1"))

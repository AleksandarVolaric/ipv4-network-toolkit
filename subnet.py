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




def network_address(address, prefix):
    mask = cidr_to_mask(prefix)
    address_octets = [int(octet) for octet in address.split(".")]
    mask_octets = [int(octet) for octet in mask.split(".")]
    network_octets = [str(address_octets[i] & mask_octets[i]) for i in range(4)]
    return ".".join(network_octets)

def broadcast_address(address, prefix):
    mask = cidr_to_mask(prefix)
    address_octets = [int(octet) for octet in address.split(".")]
    mask_octets = [int(octet) for octet in mask.split(".")]
    broadcast_octets = [str(address_octets[i] | (255 - mask_octets[i])) for i in range(4)]
    return ".".join(broadcast_octets)


def first_usable_host_address(network_address, prefix):
    if int(prefix) >= 31:
        return network_address

    octets = [int(octet) for octet in network_address.split(".")]

    for i in range(3, -1, -1):
        if octets[i] < 255:
            octets[i] += 1
            break
        octets[i] = 0
    else:
        raise ValueError("Cannot increment the maximum IPv4 address.")

    return ".".join(str(octet) for octet in octets)

def last_usable_host_address(broadcast_address, prefix):
    if int(prefix) >= 31:
        return broadcast_address

    octets = [int(octet) for octet in broadcast_address.split(".")]

    for i in range(3, -1, -1):
        if octets[i] > 0:
            octets[i] -= 1
            break
        octets[i] = 255
    else:
        raise ValueError("Cannot decrement the minimum IPv4 address.")

    return ".".join(str(octet) for octet in octets)



def total_addresses(prefix):
    prefix = int(prefix)
    return 2 ** (32 - prefix)

def total_usable_addresses(prefix):
    prefix = int(prefix)
    if prefix <= 30:
        return total_addresses(prefix) - 2
    elif prefix == 31:
        return 2  # Both addresses are usable in a /31 subnet
    else:  # prefix == 32
        return 1
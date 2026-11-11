import tkinter as tk
from tkinter import ttk

from ipv4 import (
    classify_ipv4_address,
    ipv4_to_bin,
    ipv4_to_dec,
    validate_binary_ipv4,
    validate_cidr,
)
from subnet import (
    broadcast_address,
    cidr_to_mask,
    first_usable_host_address,
    last_usable_host_address,
    mask_to_cidr,
    network_address,
    total_addresses,
    total_usable_addresses,
    validate_subnet_mask,
    wildcard_mask,
)



def main():
    """Create and run the graphical interface."""
    window = tk.Tk()
    window.title("IPv4 Network Toolkit")
    window.geometry("650x750")

    title = ttk.Label(window, text="IPv4 Network Toolkit")
    title.pack(pady=10)

    address_label = ttk.Label(window, text="IPv4 address with CIDR prefix:")
    address_label.pack(pady=5)

    address_entry = ttk.Entry(window, width=30)
    address_entry.pack(pady=5)

    result_text = tk.StringVar()
    result_label = ttk.Label(window, textvariable=result_text, justify="left")
    result_label.pack(pady=10)

    def analyze():
        user_input = address_entry.get()
        error = validate_cidr(user_input)

        if error is not None:
            result_text.set(error)
            return

        address, prefix = user_input.split("/")
        network = network_address(address, prefix)
        broadcast = broadcast_address(address, prefix)

        results = [
            f"IPv4 address: {address}",
            f"CIDR prefix: /{prefix}",
            f"Binary address: {ipv4_to_bin(address)}",
            f"Subnet mask: {cidr_to_mask(prefix)}",
            f"Wildcard mask: {wildcard_mask(prefix)}",
            f"Network address: {network}",
            f"Broadcast address: {broadcast}",
            f"First usable host: {first_usable_host_address(network, prefix)}",
            f"Last usable host: {last_usable_host_address(broadcast, prefix)}",
            f"Total addresses: {total_addresses(prefix)}",
            f"Usable hosts: {total_usable_addresses(prefix)}",
            f"IPv4 classification: {classify_ipv4_address(address)}",
        ]
        result_text.set("\n".join(results))

    analyze_button = ttk.Button(window, text="Analyze", command=analyze)
    analyze_button.pack(pady=10)

    def clear():
        address_entry.delete(0, tk.END)
        result_text.set("")

    clear_button = ttk.Button(window, text="Clear", command=clear)
    clear_button.pack(pady=5)

    conversion_frame = ttk.LabelFrame(window, text="Conversions", padding=10)
    conversion_frame.pack(fill="x", padx=10, pady=10)

    first_conversion_row = ttk.Frame(conversion_frame)
    first_conversion_row.pack(fill="x")
    second_conversion_row = ttk.Frame(conversion_frame)
    second_conversion_row.pack(fill="x", pady=(10, 0))

    decimal_binary_frame = ttk.Frame(first_conversion_row, padding=5)
    decimal_binary_frame.pack(side="left", fill="both", expand=True)

    def convert_to_binary():
        address = conversion_entry.get().strip()
        error = validate_cidr(f"{address}/32")

        if error is not None:
            conversion_result.set(error)
        else:
            conversion_result.set(f"Binary address: {ipv4_to_bin(address)}")

    conversion_label = ttk.Label(
        decimal_binary_frame,
        text="Decimal IPv4 address to convert to binary:",
        wraplength=280,
    )
    conversion_label.pack(pady=5)

    conversion_entry = ttk.Entry(decimal_binary_frame, width=30)
    conversion_entry.pack(pady=5)

    conversion_result = tk.StringVar()
    conversion_result_label = ttk.Label(
        decimal_binary_frame,
        textvariable=conversion_result,
        wraplength=280,
    )
    conversion_result_label.pack(pady=5)

    conversion_button = ttk.Button(
        decimal_binary_frame,
        text="Convert to Binary",
        command=convert_to_binary,
    )
    conversion_button.pack(pady=5)

    binary_decimal_frame = ttk.Frame(first_conversion_row, padding=5)
    binary_decimal_frame.pack(side="left", fill="both", expand=True)

    def convert_to_decimal():
        binary_address = binary_entry.get().strip()
        error = validate_binary_ipv4(binary_address)

        if error is not None:
            binary_result.set(error)
        else:
            binary_result.set(f"Decimal address: {ipv4_to_dec(binary_address)}")

    binary_label = ttk.Label(
        binary_decimal_frame,
        text="Binary IPv4 address to convert to decimal:",
        wraplength=280,
    )
    binary_label.pack(pady=5)

    binary_entry = ttk.Entry(binary_decimal_frame, width=35)
    binary_entry.pack(pady=5)

    binary_result = tk.StringVar()
    binary_result_label = ttk.Label(
        binary_decimal_frame,
        textvariable=binary_result,
        wraplength=280,
    )
    binary_result_label.pack(pady=5)

    binary_button = ttk.Button(
        binary_decimal_frame,
        text="Convert to Decimal",
        command=convert_to_decimal,
    )
    binary_button.pack(pady=5)

    prefix_mask_frame = ttk.Frame(second_conversion_row, padding=5)
    prefix_mask_frame.pack(side="left", fill="both", expand=True)

    def convert_prefix_to_mask():
        prefix = prefix_entry.get().strip()
        error = validate_cidr(f"0.0.0.0/{prefix}")

        if error is not None:
            prefix_result.set(error)
        else:
            prefix_result.set(f"Subnet mask: {cidr_to_mask(prefix)}")

    prefix_label = ttk.Label(
        prefix_mask_frame,
        text="CIDR prefix to convert to a subnet mask:",
        wraplength=280,
    )
    prefix_label.pack(pady=5)

    prefix_entry = ttk.Entry(prefix_mask_frame, width=15)
    prefix_entry.pack(pady=5)

    prefix_result = tk.StringVar()
    prefix_result_label = ttk.Label(
        prefix_mask_frame,
        textvariable=prefix_result,
        wraplength=280,
    )
    prefix_result_label.pack(pady=5)

    prefix_button = ttk.Button(
        prefix_mask_frame,
        text="Convert to Subnet Mask",
        command=convert_prefix_to_mask,
    )
    prefix_button.pack(pady=5)

    mask_prefix_frame = ttk.Frame(second_conversion_row, padding=5)
    mask_prefix_frame.pack(side="left", fill="both", expand=True)

    def convert_mask_to_prefix():
        subnet_mask = mask_entry.get().strip()
        error = validate_subnet_mask(subnet_mask)

        if error is not None:
            mask_result.set(error)
        else:
            mask_result.set(f"CIDR prefix: /{mask_to_cidr(subnet_mask)}")

    mask_label = ttk.Label(
        mask_prefix_frame,
        text="Subnet mask to convert to a CIDR prefix:",
        wraplength=280,
    )
    mask_label.pack(pady=5)

    mask_entry = ttk.Entry(mask_prefix_frame, width=30)
    mask_entry.pack(pady=5)

    mask_result = tk.StringVar()
    mask_result_label = ttk.Label(
        mask_prefix_frame,
        textvariable=mask_result,
        wraplength=280,
    )
    mask_result_label.pack(pady=5)

    mask_button = ttk.Button(
        mask_prefix_frame,
        text="Convert to CIDR",
        command=convert_mask_to_prefix,
    )
    mask_button.pack(pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
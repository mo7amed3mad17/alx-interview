#!/usr/bin/python3
"""
Validate-UTF-8
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    # `0b10000000` (0x80) mask to check if the highest bit is set.
    # `0b11000000` (0xC0) mask to check if the two highest bits are 10.

    for byte in data:
        # Only the least significant 8 bits are needed for each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes based on the first byte
            if (byte >> 7) == 0:       # 1-byte character
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid first byte
        else:
            # Check if the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, we are missing continuation bytes
    return num_bytes == 0

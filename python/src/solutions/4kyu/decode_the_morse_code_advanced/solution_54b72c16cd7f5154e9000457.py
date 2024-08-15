"""https://www.codewars.com/kata/decode-the-morse-code-advanced"""

from preloaded import MORSE_CODE


def decode_bits(bits: str):
    bits = bits.strip("0")

    consecutive_bit_counts = []
    consecutive_count = 0
    previous_bit = bits[0]

    for bit in bits:
        if bit == previous_bit:
            consecutive_count += 1
        else:
            consecutive_bit_counts.append(consecutive_count)
            consecutive_count = 1
        previous_bit = bit
    consecutive_bit_counts.append(consecutive_count)

    bits_per_dot = min(consecutive_bit_counts)

    return bits.replace('0000000' * bits_per_dot, "   ") \
        .replace('111' * bits_per_dot, '-') \
        .replace('000' * bits_per_dot, ' ') \
        .replace('1' * bits_per_dot, '.') \
        .replace('0' * bits_per_dot, '')


def decode_morse(morse_code):
    return " ".join(
        ["".join([MORSE_CODE[letter] for letter in word.split(" ")]) for word in morse_code.split("   ")]).strip()

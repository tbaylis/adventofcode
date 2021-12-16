"""
Advent of code, day 16 - Packet Decoder

https://adventofcode.com/2021/day/16
"""
import fileinput
import operator
import functools

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex2bin_str(s):
    return "".join(hex2bin[c] for c in s)


def parse_packet_literal(bits):
    value = ""

    is_last_group = bits[0] != "1"

    while not is_last_group:
        value += bits[1:5]
        bits = bits[5:]
        is_last_group = bits[0] != "1"
    if is_last_group:
        value += bits[1:5]

    return int(value, base=2), bits[5:]


def parse_sub_packets(bits):
    length_type_id = int(bits[0], base=2)
    bits = bits[1:]
    total_packet_version = 0
    values = []

    if length_type_id == 0:
        length_sub_packet = int(bits[:15], base=2)

        bits = bits[15:]
        subbits = bits[:length_sub_packet]

        while len(subbits) > 6:
            value, subbits, subtotal_packet_version = parse_packet(subbits)
            values.append(value)
            total_packet_version += subtotal_packet_version
        bits = bits[length_sub_packet:]

    if length_type_id == 1:
        number_of_sub_packets = int(bits[:11], base=2)

        bits = bits[11:]

        for _ in range(number_of_sub_packets):

            value, bits, subtotal_packet_version = parse_packet(bits)
            values.append(value)
            total_packet_version += subtotal_packet_version

    return values, bits, total_packet_version


def parse_packet(bits):
    packet_version = int(bits[:3], base=2)
    packet_type = int(bits[3:6], base=2)
    bits = bits[6:]

    if packet_type == 4:
        value, bits = parse_packet_literal(bits)
        return value, bits, packet_version

    # Operator packet
    values, bits, sub_total = parse_sub_packets(bits)

    if packet_type == 0:
        # sum
        value = sum(values)

    if packet_type == 1:
        # product
        value = functools.reduce(operator.mul, values)

    if packet_type == 2:
        # minimum
        value = min(values)

    if packet_type == 3:
        # max
        value = max(values)

    if packet_type == 5:
        # greater than
        value = 1 if values[0] > values[1] else 0

    if packet_type == 6:
        # less than
        value = 1 if values[0] < values[1] else 0

    if packet_type == 7:
        # equals
        value = 1 if values[0] == values[1] else 0

    return value, bits, packet_version + sub_total


if __name__ == "__main__":

    assert parse_packet(hex2bin_str("620080001611562C8802118E34"))[2] == 12
    assert parse_packet(hex2bin_str("D2FE28"))[0] == 2021
    assert parse_packet(hex2bin_str("38006F45291200"))[0] == 1
    assert parse_packet(hex2bin_str("EE00D40C823060"))[0] == 3
    assert parse_packet(hex2bin_str("8A004A801A8002F478"))[2] == 16
    assert parse_packet(hex2bin_str("C0015000016115A2E0802F182340"))[2] == 23
    assert parse_packet(hex2bin_str("A0016C880162017C3686B18A3D4780"))[2] == 31

    assert parse_packet(hex2bin_str("C200B40A82"))[0] == 3
    assert parse_packet(hex2bin_str("04005AC33890"))[0] == 54
    assert parse_packet(hex2bin_str("880086C3E88112"))[0] == 7
    assert parse_packet(hex2bin_str("CE00C43D881120"))[0] == 9
    assert parse_packet(hex2bin_str("D8005AC2A8F0"))[0] == 1
    assert parse_packet(hex2bin_str("F600BC2D8F"))[0] == 0
    assert parse_packet(hex2bin_str("9C005AC2F8F0"))[0] == 0
    assert parse_packet(hex2bin_str("9C0141080250320F1802104A08"))[0] == 1

    for line in fileinput.input():
        value, _, total_packet_version = parse_packet(hex2bin_str(line.strip()))
        print(f"{total_packet_version=}, {value=}")

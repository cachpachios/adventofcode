from utils import *
import sys
import string
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)

packet = ''.join([format(int(x,16), "04b") for x in list(file[0])])

def parse_operator(s):
    packets = []
    if s[0] == '1':
        num_subpackets = int(s[1:12],2)
        print("OPERATOR, NUM SUBPACKETS", num_subpackets)
        s = s[12:]
        for i in range(num_subpackets):
            packet, s = parse_packet(s)
            packets.append(packet)
        return packets, s
    else:
        num_data = int(s[1:16],2)
        print("OPERATOR, DATA", num_data)
        s = s[16:]
        buf = len(s) - num_data
        while len(s) > buf:
            packet, s = parse_packet(s)
            packets.append(packet)
        return packets, s


def parse_literal(s):
    i = 0
    int_s = ''
    while True:
        int_s += s[i+1:i+5]
        if s[i] == "0":
            break
        i += 5
    return int(int_s, 2), s[i+5:]

versions = []

def parse_packet(s):
    print("PACKET", s)
    version = int(s[:3], 2)
    id = int(s[3:6], 2)
    versions.append(version)

    if id == 4:
        return parse_literal(s[6:])
    else:
        packets, s = parse_operator(s[6:])

        match id:
            case 0:
                return all_sum(packets), s
            case 1:
                return all_prod(packets), s
            case 2:
                return all_min(packets), s
            case 3:
                return all_max(packets), s
            case 5:
                assert len(packets) == 2
                return 1 if packets[0] > packets[1] else 0, s
            case 6:
                assert len(packets) == 2
                return 1 if packets[0] < packets[1] else 0, s
            case 7:
                assert len(packets) == 2
                return 1 if packets[0] == packets[1] else 0, s


result, left = parse_packet(packet)

# answer = sum(versions)
answer = result
print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
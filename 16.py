from dataclasses import dataclass
from math import prod

from utils import rinput

HEX2BIN = str.maketrans(
    {
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
)


@dataclass
class Literal:
    version: int
    type_id: int
    value: int


@dataclass
class Operator:
    version: int
    type_id: int
    subpackets: list


def parse_packet(bin_str):
    version = int(bin_str[:3], 2)
    type_id = int(bin_str[3:6], 2)
    if type_id == 4:
        body = bin_str[6:]
        groups = []
        while True:
            groups.append(body[1:5])
            prefix = body[0]
            body = body[5:]
            if prefix == "0":
                break
        value = int("".join(groups), 2)
        return Literal(version, type_id, value), body
    else:
        length_type_id = int(bin_str[6], 2)
        body = bin_str[7:]
        if length_type_id == 0:
            subpacket_length = int(body[:15], 2)
            body, rest = (
                body[15 : 15 + subpacket_length],
                body[15 + subpacket_length :],
            )
            subpackets = []
            while body:
                subpacket, body = parse_packet(body)
                subpackets.append(subpacket)
            return Operator(version, type_id, subpackets), rest
        else:
            num_subpackets = int(body[:11], 2)
            body = body[11:]
            subpackets = []
            for _ in range(num_subpackets):
                subpacket, body = parse_packet(body)
                subpackets.append(subpacket)
            return Operator(version, type_id, subpackets), body


def sum_versions(packet):
    match packet:
        case Literal(version, _, _):
            return version
        case Operator(version, _, packets):
            return version + sum(sum_versions(subpacket) for subpacket in packets)


def eval_packet(packet):
    match packet:
        case Literal(_, _, value):
            return value
        case Operator(_, 0, packets):
            return sum(eval_packet(p) for p in packets)
        case Operator(_, 1, packets):
            return prod(eval_packet(p) for p in packets)
        case Operator(_, 2, packets):
            return min(eval_packet(p) for p in packets)
        case Operator(_, 3, packets):
            return max(eval_packet(p) for p in packets)
        case Operator(_, 5, [fst, snd]):
            return int(eval_packet(fst) > eval_packet(snd))
        case Operator(_, 6, [fst, snd]):
            return int(eval_packet(fst) < eval_packet(snd))
        case Operator(_, 7, [fst, snd]):
            return int(eval_packet(fst) == eval_packet(snd))


packet, _ = parse_packet(rinput(16).strip().translate(HEX2BIN))
print(sum_versions(packet))
print(eval_packet(packet))

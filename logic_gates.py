def not_gate(bit):
    if bit == 0:
        return 1
    else:
        return 0

def and_gate(bit_a, bit_b):
    if (bit_a and bit_b) == 1:
        return 1
    else:
        return 0

def or_gate(bit_a, bit_b):
    if (bit_a or bit_b) == 0:
        return 0
    else:
        return 1

def nor_gate(bit_a, bit_b):
    if (bit_a and bit_b) == 0:
        return 1
    else:
        return 0

def nand_gate(bit_a, bit_b):
    if (bit_a and bit_b) == 1:
        return 0
    else:
        return 1

def xor_gate(bit_a, bit_b):
    return and_gate(or_gate(bit_a, bit_b), nand_gate(bit_a, bit_b))

def xnor_gate(bit_a, bit_b):
    return not_gate(xor_gate(bit_a, bit_b))



from logic_gates import *

def half_adder(first_bit, second_bit): 
    return [ and_gate(first_bit, second_bit), xor_gate(first_bit, second_bit) ]

def full_adder(carry_in, bit_a, bit_b):
    first_ha = half_adder(bit_a, bit_b)
    second_ha = half_adder(carry_in, first_ha[1])
    return [ or_gate(second_ha[0], first_ha[0]),second_ha[1] ] 

def adder(a_number, b_number):
    x = 0
    summa = []
    for i in range(-1, -9, -1):
        m_result = full_adder(x, a_number[i], b_number[i])
        summa.append(m_result[1])
        x = m_result[0]
    return [i for i in summa[::-1]]

def user_input():
    a = input()
    if len(a) < 8:
        a = '0' * (8 - len(a)) + a
    return [int(i) for i in a]
        
      
if __name__ == '__main__':
    print(adder(user_input(), user_input()))



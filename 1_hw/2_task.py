import secrets

qty_bits_list = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

for qty_bits in qty_bits_list:
    bits = secrets.randbits(qty_bits)
    bits_hex = hex(bits)
    # private_key = bits_hex[2:]
    print(f'Example key in {qty_bits} bit sequence: {bits_hex}')

if __name__ == '__main__':
    pass

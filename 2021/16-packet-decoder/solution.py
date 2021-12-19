import sys

# type ID 4 - literal
# type ID others - operator
#   depends on length type ID
        # - 0 15 bits total length in bits of subpackets
        # - 1 11 bites number of number of subpackets

# with open(sys.argv[1], 'r') as f:
#     s = next(f).strip()

s = sys.argv[1]
allbits = '{:b}'.format(int(s, 16))

def sum_packet_versions(bs: str, sub: bool):
    nbits = len(bs)
    i = 0

    version_sum = 0
    while i < nbits:
        if int(bs[i:], 2) == 0:# hex encoding end padding
            break
        # process each packet
        version = int(bs[i:i+3], 2)
        # print(f"{i=} {version=} {len(bs)=}")
        version_sum += version
        i += 3
        type_id = int(bs[i:i+3], 2)
        i += 3
        if type_id == 4:
            while int(bs[i]) == 0:
                if sub and len(bs[i:]) == 5: # last block is first block
                    break
                i += 1  # skip left padded for literal
            literal_val_s = ""
            while int(bs[i]) == 1:
                i += 1
                literal_val_s += bs[i:i+4]
                i += 4
            i += 1  # 0 end literal block
            literal_val_s += bs[i:i+4]  # trailing zero pads
            i += 4
            
            break # the input packet has to end with type 4
        else:
            len_type_id = int(bs[i])
            i += 1
            if len_type_id == 0:
                sub_len_in_bits = int(bs[i:i+15], 2)
                i += 15
                version_sum += sum_packet_versions(bs[i:i+sub_len_in_bits], True)
                i += sub_len_in_bits
            elif len_type_id == 1:
                no_of_sub = int(bs[i:i+11], 2)
                i += 11
            else:
                raise ValueError(f"Parsing error {i=}")
    return version_sum

version_sum = sum_packet_versions(allbits, False)
print(version_sum)
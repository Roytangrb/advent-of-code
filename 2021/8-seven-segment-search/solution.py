unique_signal_count = {
    2: '1',
    4: '4',
    3: '7',
    # 5: ['2', '3', '5']
    # 6: ['0', '6', '9']
    7: '8',
}
signal_map = {
    '0': 'abcefg', #
    '1': 'cf', #
    '2': 'acdeg', 
    '3': 'acdfg',
    '4': 'bcdf', #
    '5': 'abdfg', #
    '6': 'abdefg', #
    '7': 'acf', #
    '8': 'abcdefg', #
    '9': 'abcdfg', #
}
entries = []

with open('input2.txt', 'r') as f:
    for line in f:
        patterns, digits = [d.strip() for d in line.split("|")]
        entries.append((patterns.split(), digits.split()))

def ss(s):
    return "".join(sorted(list(s)))

ans1 = 0
ans2 = 0
for patterns, digits in entries:
    found = {}
    i_pattern = {}
    not_found5 = []
    not_found6 = []
    for pattern in patterns:
        l = len(pattern)
        if l in unique_signal_count:
            found[ss(pattern)] = unique_signal_count[l]
            i_pattern[unique_signal_count[l]] = pattern
        elif l == 5:
            not_found5.append(pattern)
        else:
            not_found6.append(pattern)
    
    for nf in not_found6:
        p2 = set(i_pattern['1'])
        p4 = set(i_pattern['4'])
        p7 = set(i_pattern['8'])
        snf = ss(nf)
        chs = set(nf)
        if ((p7 - chs) & p2):
            found[snf] = '6'
            i_pattern['6'] = nf
        elif ((p7 - chs) & p4):
            found[snf] = '0'
            i_pattern['0'] = nf
        else:
            found[snf] = '9'
            i_pattern['9'] = nf
    
    for nf in not_found5:
        p6 = set(i_pattern['6'])
        p9 = set(i_pattern['9'])
        snf = ss(nf)
        chs = set(nf)
        if not ((p6 - chs) & p9):
            found[snf] = '5'
        elif len((p9 - chs)) == 1:
            found[snf] = '3'
        else:
            found[snf] = '2'
        
    # print(found)
    decoded = ""
    for digit in digits:
        if len(digit) in unique_signal_count:
            ans1 += 1
            decoded += unique_signal_count[len(digit)]
        else:
            decoded += found[ss(digit)]
    # print(decoded)
    ans2 += int(decoded)

# print(ans1)
print(ans2)
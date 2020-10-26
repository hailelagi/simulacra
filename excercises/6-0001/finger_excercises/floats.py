bin_num = str(10011)
hex_num = 0

s = len(bin_num)
bin_pow = len(bin_num) - 1

for i in range(s):
    hex_num += int(bin_num[i]) * 2 ** bin_pow
    bin_pow -= 1

print(hex_num)

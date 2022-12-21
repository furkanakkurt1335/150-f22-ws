# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
fh = open(filename, 'r')
body = fh.read()

first_char_d = dict()
for word in body.split(' '):
    f_ch = word[0]
    if f_ch not in first_char_d.keys():
        first_char_d[f_ch] = 0
    first_char_d[f_ch] += 1

char_l = sorted(list(first_char_d.keys()))
for ch in char_l:
    print(ch, first_char_d[ch])

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
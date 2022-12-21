# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
fh = open(filename, 'r')
body = fh.read().lower().replace(',', '').replace('.', '')

word_d = dict()
limit = 2
body_l = list()
for word in body.split(' '):
    if word not in word_d.keys():
        word_d[word] = 0
    word_d[word] += 1
    if word_d[word] <= limit:
        body_l.append(word)

new_str = ' '.join(body_l)

word_l = list(word_d.keys())
for key in word_l:
    if word_d[key] <= limit:
        del word_d[key]

word_l = sorted(list(word_d.keys()))

for word in word_l[2:]:
    print(word, word_d[word])

print(new_str)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

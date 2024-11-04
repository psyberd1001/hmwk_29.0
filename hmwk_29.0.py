from itertools import permutations


def all_variants(text):
    for i in range(len(text)):
        for line in range(len(text) - i):
            yield text[line:i + line + 1]


a = all_variants("abc")
for i in a:
    print(i)

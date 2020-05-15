import re
pattern = '[\d]+'
st = input()
st1 = re.search(pattern, st)
st2=(st1.group())
print(list(st2))
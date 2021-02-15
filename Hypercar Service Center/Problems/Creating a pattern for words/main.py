from nltk.tokenize import regexp_tokenize

text = input()
pos = int(input())
print(regexp_tokenize((text), r"[A-z]+")[pos])

data = input()
word = input()
i = 0
result = 0
while i <= len(data)-len(word):
    if data[i:i+len(word)] == word:
        result += 1
        i += len(word)
    else:
        i += 1
print(result)

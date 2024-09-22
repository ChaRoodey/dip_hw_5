def substrings(s: str):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]


s = input('Введите строку: ')
print('Возможные подстроки: ')

for i in substrings(s):
    print(i)
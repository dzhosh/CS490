# 1
odds = (1, 3, 5, 7, 9)
for num in range(100, 501):
    if num % 10 in odds:
        if num // 100 in odds:
            if num // 10 % 10 in odds:
                print(num)
print()


# 2
string_list = ["1", "4", "0", "6", "9"]
int_list = []

for s in string_list:
    int_list.append(int(s))
int_list.sort()
print(int_list, '\n')


# 3
infile = open("input.txt")
for line in infile:
    words = 1
    letters = 0
    previous = ' '

    for c in line:
        if c == ' ':
            if previous != ' ':
                words += 1
        elif c.isalpha():
            letters += 1
        previous = c

    if line.endswith('\n'):
        line = line[:-1]
    print(line, " ---> Words: ", words, "  Letters: ", letters)

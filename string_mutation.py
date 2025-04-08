def mutate(string, position, charachter):
    string = string[:position] + charachter + string[position+1:]
    return string

s = input()
i, c = input().split()
x = mutate(s, int(i), c)
print(x)

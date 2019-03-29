#Задание №14.3
x = str(input("Введите строчку: "))
def poiskslov (s):
    x1 = list(s)
    n = 0
    if x1[0] != " ":
        n = n + 1
    for i in range(len(x1)):
        if x1[i] == " " and x1[(i+1)] != " ":
            n += 1
    return n
y = poiskslov (x)
print (y)




input = 100
c3 = 0
c5 = 0
for i in range(1, input):
    c3 += 1
    c5 += 1
    output = ""
    if c3 == 3:
        output += "Fizz"
        c3 = 0
    if c5 == 5:
        output += "Buzz"
        c5 = 0
    if output == "":
        print(i)
    else:
        print(output)

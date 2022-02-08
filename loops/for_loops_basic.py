for x in range(1,151):
    print(x)

for x in range(5,1005,5):
    print(x)

def count_X():
    for x in range(0,101):
        if x % 5 == 0:
            print('coding')
        if x % 10 == 0:
            print('coding dojo')
        else:
            print(x)
count_X()


sum = 0
for x in range(1,500001,2):
        sum += x
print(sum)

for x in range(2018,0,-4):
    print(x)


def x_counterdown(low, high, mult):
    for x in range (low, high + 1):
        if x % mult == 0:
            print(x)

x_counterdown(2, 9, 3)
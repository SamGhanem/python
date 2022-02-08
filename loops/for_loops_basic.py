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


low_num = 2
high_num = 9
mult = 3
for x in range(low_num,high_num + 1):
    if x % mult == 0:
        print(x)

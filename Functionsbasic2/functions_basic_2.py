#1 COUNtddown
for x in range(5, 0, -1):
    print(x)

#2 Print and Return
x = 1
print(x)
def print_and_return():
    x = 2
    return(2)
x = print_and_return()
print(x)

# 3 First Plus Length
def first_plus_length(some_list):
    return (some_list[0] + len(some_list))
print(first_plus_length([1,2,3,4,5]))

#4 Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        newlist = []
        #this is a new list for new values 
        for i in range(0,len(list)):
            # print(list[i])
            if list[i] > list[1]:
                # print(list[i])
                newlist.append(list[i])
        #how many values are in this list
        #return the new list 
        print(len(newlist))
        return newlist
print(values_greater_than_second([1,3,4,2,523,9,1]))
print(values_greater_than_second([1]))
print(values_greater_than_second([1,3,4,2,523,9,1,45,6,453,234,523452,2134]))


#5 This Length, That Value
def length_and_value(size,value):
    newlist = []
    for i in range(size):
        newlist.append(value)
    return newlist
print(length_and_value(7,999))
print(length_and_value(6,8787))



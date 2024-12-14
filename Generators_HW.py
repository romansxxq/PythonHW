start = int(input("Enter start num: "))
end = int(input("Enter end num: "))

def odd_num(start,end):
    for i in range(start,end):
        if i % 2 != 0:
            yield i


for i in odd_num(start,end):
    print(i)
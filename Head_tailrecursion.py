
def head(n):
    if n==0:
        return
    head(n-1)
    print(n)
num=int(input("enter a number:"))
head(num)

def tail(n):
    if n==0:
        return
    print(n)
    tail(n-1)
num=int(input("enter the number:"))
tail(num)
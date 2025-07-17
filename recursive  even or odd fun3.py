def one(n):
    if n==0:
        return True
    else:
        return two(n-1)
def two(n):
    if n==0:
        return False
    else:
        return one(n-1)
num=int(input("enter a number:"))
if one(num):
    print(num,"It is even number")
else:
    print(num,"It is odd number")
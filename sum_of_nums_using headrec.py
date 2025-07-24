def sumhead(n):
    if n==0:
        return n
    return n+sumhead(n-1)
num=int(input("enter a number:"))
print("sum:",sumhead(num))
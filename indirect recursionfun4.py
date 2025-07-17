def A(n):
    if n<=0:
        return
    print("Ravi",n)
    B(n-1)
def B(n):
    if n<=0:
        return
    print("Dwarapudi",n)
    A(n-1)
num=int(input("enter a number:"))
A(num)

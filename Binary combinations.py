def binary(l,b=' '): #2, ' ' ! '0' #0, 00 #1 ,0
    if l==0: #true
        print(b)
        return
    print(l,"l value before 1st functon")
    binary(l-1,b+'0') #1,' 0" #0,00 10
    print(l,"l value after 1st function")
    binary(l-1,b+'1')

length=int(input("enter the length of binary numbers"))#2
print("Binary combinations.....")
binary(length)#2
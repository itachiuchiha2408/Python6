a=int(input("Enter a:"))
file=open("factorialnum.txt",'w')
file.write("Enter Number:")
file.write(str(a))
file.write('\n')
fact=1
while(a>0):
    fact=fact*a
    a=a-1
print(fact)
file.write("Factorial of Number is,")
file.write(str(fact))

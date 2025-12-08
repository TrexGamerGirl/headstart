
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Entrt 3rd number: '))

if(c < a > b):
 print(" The first number is larger")
elif c < b > a :
    print("The second number is larger")
elif(a < c > b):
    print("The third number is larger")
elif a == b == c:
    print("they are the same value")
elif a == b > c:
    print(" the first and second numbers are biggest")
elif a == c > b:
    print(" the first and third numbers are biggest")
elif c == b > a:
    print(" the third and second numbers are biggest")
else:
    print('something went wrong')
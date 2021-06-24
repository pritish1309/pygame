a=int(input('Enter your first number : '))
b=int(input('Enter your second number : '))
def GCD(a,b):
    if a>b:
        small=a
        big=b
    else :
        small=b
        big=a
        
    while big%small!=0:
        remainder=big%small
        big=small
        small=remainder
    return (small)

print(GCD(a,b))

a=int(input('Please enter your first number'))
b=int(input('Please enter your second number'))
c=int(input('Please enter your third number'))
if a>b and a>c:
    if b>c:
        print(a,'is the largest,',b,'is in the middle and',c,'is the smallest')
    else:
        print(a,'is the largest,',c,'is in the middle and',b,'is the smallest')
if b>c and b>a:
    if c>a:
        print(b,'is the largest,',c,'is in the middle and',a,'is the smallest')
    else:
        print(b,'is the largest,',a,'is in the middle and',c,'is the smallest')
if c>a and c>b:
    if a>b:
        print(c,'is the largest,',a,'is in the middle and',b,'is the smallest')
    else:
        print(c,'is the largest,',b,'is in the middle and',a,'is the smallest')

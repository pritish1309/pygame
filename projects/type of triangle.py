#This is a code to identify the type of triangle formed on entering 3 angles
a=int(input('Please enter your first angle :'))
b=int(input('Please enter your second angle :'))
c=int(input('Please enter your third angle :'))
if a+b+c==180 and a>0 and b>0 and c>0:
    if a==60 and b==60 and c==60:
        print('The triangle is formed is an Equilateral Triangle')
    else:
        if a!=b and b!=c and a!=c:
            if a>90 or b>90 or c>90:
                print('The triangle so formed is an Obtuse Angled Scalene Triangle')
            else:
                if a==90 or b==90 or c==90:
                    print('The triangle so formed is a Right Angled Scalene Triangle')
                else:
                    print('The triangle so formed is an Acute Angled Scalene Triangle')
        if a==b!=c or b==c!=a or c==a!=b:
            if a>90 or b>90 or c>90:
                print('The triangle so formed is an Obtuse Angled Isosceles Triangle')
            else:
                if a==90 or b==90 or c==90:
                    print('The triangle so formed is a Right Angled Isoscles Triangle')
                else:
                    print('The triangle so formed is an Acute Angled Isosceles Triangle')

else:
    if a+b+c>180:
        print('The angle sprovided by you cannot form a triangle')
        print('To form a triangle, the sum of the 3 angles provided by you should be',a+b+c-180,'degrees less')
    else:
       print('The angle sprovided by you cannot form a triangle')
       print('To form a triangle, the sum of the 3 angles provided by you should be',180-a-b-c,'degrees more') 
        
        
    
    
    
    

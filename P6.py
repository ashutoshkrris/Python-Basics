import cmath

a = int(input("Enter the co-efficient of x^2 : "))
b = int(input("Enter the co-efficient of x : "))
c = int(input("Enter the constant : "))
d = (b*b)-(4*a*c)
r1 = (-b-cmath.sqrt(d))/(2*a)
r2 = (-b+cmath.sqrt(d))/(2*a)
print("The roots are "+str(r1)+" and "+str(r2))


'''                                         Output
                            Enter the co-efficient of x^2 : 1
                            Enter the co-efficient of x : 4
                            Enter the constant : 4
                            The roots are (-2+0j) and (-2+0j)
                                            OR
                            Enter the co-efficient of x^2 : 3
                            Enter the co-efficient of x : 4
                            Enter the constant : 5
                            The roots are (-0.6666666666666666-1.1055415967851332j) and (-0.6666666666666666+1.1055415967851332j)
'''
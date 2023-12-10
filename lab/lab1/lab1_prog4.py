# Enter two complex variables z1 & z2. Find the equivalent impedance when z1 & z2 are connected in parallel
import cmath

x1 = int(input())            # first variable real part
y1 = int(input())            # first variable imaginary part
x2 = int(input())            # second variable real part
y2 = int(input())            # second variable imaginary part

cn1 = complex(x1,y1)
cn2 = complex(x2,y2)

ans = cn1*cn2 / (cn1+cn2)
print("Required complex impedance is :")
print(ans)

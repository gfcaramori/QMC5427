First problems

**Problem - 1**
operators:
Floor division operators
~~~/python
x = 45
y = 14
z = x // y
print(z)
r = y % z
print(x)
t = 10
print(z + t)
print('z = x // y =', z)
~~~

**Problem - 2**
Creating solver for a $$ax^2 + bx + c =0$$ equation

~~~python
import math
print("entre com os valores dos coeficientes a, b, e c: ")
a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
delta = (b**2) - (4*a*c)
if delta  < 0:
    print("A equação não possui raízes reais")
    raizDelta = math.sqrt(abs(delta))*(0 + 1j)
    x_1 = (-b + raizDelta)/(2*a)
    x_2 = (-b - raizDelta)/(2*a)
    print("As raízes complexas são x_1 = {0} e x_2 = {1}" .format(x_1, x_2))
elif delta == 0 :
    x = (-b)/(2*a)
    print ("A equaçao possui apenas uma raíz x = {0}" .format(x))
elif delta > 0 :
    raizDelta = math.sqrt(delta)
    x_1 = (-b + raizDelta)/(2*a)
    x_2 = (-b - raizDelta)/(2*a)
    print("As raízes obtidas são x_1 = {0} e x_2 = {1}" .format(x_1, x_2))
~~~

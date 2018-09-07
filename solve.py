import math

a = int(raw_input("A:"))
b = int(raw_input("B:"))
c = int(raw_input("C:"))

first_term = b/(2.0*a)
second_term = math.sqrt(b**2 - 4*a*c)/(2.0*a)

print -first_term + second_term, "or", -first_term - second_term

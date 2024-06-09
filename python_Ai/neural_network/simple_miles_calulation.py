
import numpy

c = float(input("enter the value of c: "))
k = float(input("enter the value of kilometers: "))
print(f"the value of c is {c}")
print(f"the value of kilometers are {k}")


def predict_machine():
    miles = k + c
    return miles

predicted_miles = predict_machine()
print(predicted_miles)
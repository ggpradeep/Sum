string = input("Enter a string that is going to be reversed")
string2 = ("")

for i in string:
    string2 = i + string2
print("\n Orignal string =", string)
print("\n Reversed string", string2)
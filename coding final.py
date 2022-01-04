# taking two inputs at a time
x, y = input("Enter number of boys and girls in a class").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time
x, y, z = input("Enter any three branch in a class :").split()
print("branch 1: ", x)
print("branch 2: ", y)
print("branch 3: ", z)
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(str, input("Enter student names: ").split()))
print("List of students: ", x)

#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program
y = 0 
for i in range (1,6):
    x = float(input("enter a number"))
    y = y+x
    c = y/5
    print(f"the sum of numbers is {y},averge is {c}")



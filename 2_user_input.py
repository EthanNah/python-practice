#input a name value
#name = input("Enter your name: ") #if i want to get always lower then add ".lower()"
#print(name)

#input variable for mathmatical calculate
#note: input() -> always return a str value
#then how do we change str value to int? -> input variable redefine as int

#ex)
size_input = input("Enter the square feet: ") #input value as str
square_feet = int(size_input) #redefine size input as int from str value
#if I want to input value as int not a str, then cover the input with int
#size_input = int(input("Enter the square feet: ")) 
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres} square metres.") 
#if I want to show 2 decimal points then change {square_metres} to {square_metres:.2f} 



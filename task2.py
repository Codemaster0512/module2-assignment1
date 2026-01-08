#Create a Personalized Greeting

#Takes a user's first name and last name as input.

f_name = str(input("Enter first name: "))
l_name = str(input("Enter last name: "))

#Concatenates the first name and last name into a full name.

full_name = f_name + " " + l_name

#Prints a personalized greeting message using the full name.

print('Good Morning,',full_name,'Welcome to the game!')
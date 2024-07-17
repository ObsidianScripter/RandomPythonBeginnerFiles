while True:
	# So first we create an infinite loop since true will always be true
	print("Who tf are you?")
	# then we ask for the person's name
	name = input()

	if name != "Mick": # if the person types anything besides "Mick"
		continue    # the program jumps back to the first statement
	# if "Mick" was the input then the password is asked requested
	print("Aight, so what's the password?")
# the user is asked to input the number password hence the int() function
	password = int(input())
# if the password is equal to 12345 then the program breaks and the outside
# statement is shown	
	if password == 12345:  
# if the password isn't equal to 12345 then the program restarts from 
# the top
		break 
	else:
		print("You done fucked up now")
print("You lucky lil nigga") # this is the outside statement


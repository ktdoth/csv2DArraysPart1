def main():

	# Print the Program Introduction on the Screen
	print("THE PRICE CHECKER")
	print(" ")
	print("This Program Price Checks by Item Category")
	print(" ")

	# read_CSV_File_into_Array() will go here later on

	# set loop Controller to True to get loop Started
	getMorePrices=True

	while getMorePrices ==True:

		# Ask the user if they want to Get more Price Lists
		userChoice = input("Do you need to do a Price Check ? Y/N : ")
		print(" ")

		if (userChoice == "Y" or userChoice == "y" or 
			userChoice == "Yes" or userChoice == "yes" or 
			userChoice == "YES"):
			print(" ")
			print("*** Processing Not Written Yet****")
			print(" ")
			#User_Selects_Item_Category() will go here later on
		
		else:
			getMorePrices=False
			# If they typed anything different to Y or y, then End pgm
			input("Press the Enter Key to Exit the Program")
			exit()
	
	# Input Statement to stop the Py.exe output from disappearing
	input("Press the Enter Key to Exit the Program")

# Tell Python to do the main Process
main()
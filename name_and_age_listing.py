#Initialize a list to properly store data.
profiles = [ ]
  
#Define a function for inputing a name. 
def valid_names(name):
     #Define the condition for a name to consist of only alphabet letters.
     return name.isalpha( ) and len(name) > 0
  
#Define a function for inputing an age.
def valid_ages(age):
     #Define the conditions for an age to be a positive integer greater than 0.
     return age.isdigit( ) and int(age) > 0
#Start a loop that will ask the user to input a name and an age which will stop or continue if yes or no is replied.
while True:

#Input a try variable to print an error message.
      try:
      #Ask the user to enter a name.
           name = input("Please enter a name: ")
      #Validate the name input.
           if not valid_names(name):
             #If the entry is valid, proceed. If not, ask the user to enter a name again.
              raise ValueError("The name you entered is invalid. Please enter a valid name.")
      #Ask the user to input an age.
           age = input("Please enter an age: ")
      #Validate the age input.
           if not valid_ages(age):
             #If the entry is valid, proceed. If not, ask the user to enter an age again.
              raise ValueError("The age you entered is invalid. Please enter a valid age.")
      #Store the collected information in the list.
           profiles.append((name, int(age)))
      #Ask the user if they want to continue putting in names and ages.
	   enter_another_profile = input("Do you want to input another profile? (Yes/No): ").strip( ).lower( )
      #Enter a condition where answering no stops the loop.
	   if enter_another_profile == "no":
                break
      #Enter a condition where answering not yes or no prints an error message.
           if enter_another_profile != "yes":
               	print("Invalid. Please try again.")
      #Input an except variable to print an error message.	   
      except ValueError as incorrect:
               print(incorrect)
       
#Define a variable to identify the oldest age/s.

#Define a variable to identify the names corresponding to the ages.

#Print the name and age of the oldest person entered.

#Use an if statement to go back to the defined list.

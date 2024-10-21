#Initialize a list to properly store data.
def main ( ):
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

#Input a try variable to print an error message.

#Ask the user to enter a name.

#Validate the name input.

#If the entry is valid, proceed. If not, ask the user to enter a name again.

#Ask the user to input an age.

#Validate the age input.

#If the entry is valid, proceed. If not, ask the user to enter an age again.

#Store the collected information in the list.

#Input an except variable to print an error message.

#Ask the user if they want to continue putting in names and ages.

#Define a variable to identify the oldest age/s.

#Define a variable to identify the names corresponding to the ages.

#Print the name and age of the oldest person entered.

#Use an if statement to go back to the defined list.

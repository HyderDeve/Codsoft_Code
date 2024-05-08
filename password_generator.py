import random

#create a password variable to store all characters the possible password will include

password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_:"

# now to create a variable for length of the random password

len_password=int(input("Enter The Length You Want For Your Password: "))

# variable for storing the generated password

gen_password="".join(random.sample(password,len_password)) #radnom.sample takes 2 arguments 1st the charcter dataset 
#or the place from where you wnat a random generation/choice 2nd one is the number of characters you want it to be of. 


print(gen_password)

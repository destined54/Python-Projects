from hashlib import *
login_dic = {}

def makeHash(password): #used to encypt password
	return sha256(password.encode ('utf-8')).hexdigest()

def login(login_dic): 
	username = input("Please type your username: ") 
	password = input("Please type your password: ")
	password = makeHash(password)
	
def signup(): 
	username = input("Choose a username, then type here: ")
	password = input("Type your password here: ")
	password = makeHash(password)
	
print("Login or Signup! Type L to Login or S to Signup: ")
user_input = input()
if user_input == "L":
	login()
elif user_input == "S":
	signup()
	print("Would you like to login? Type Y for yes or N for no: ")
	if user_input == "Y":
		login()
	elif user_input == "N":		
else: 
	print("Login or Signup here!")

signup()
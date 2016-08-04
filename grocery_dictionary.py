print("Welcome to Destiny's Finest: your #1 grocery store that will supply all your needs!")
groceries = {}

done = False

def add_item():
	item = input("What item would you like to add?")
	quantity = input("How many " + item + "s would you like?")
	groceries[item] = quantity	
	
def update_item():
	item = input("What item would you like to update?")
	if item in groceries:
		quantity = input("What would you like the new quantity of" + item + "to be?")
		groceries[item] = quantity
	else: 
		print("Item not found.")
		new_item = input("Would you like to add" + item + " ? Y or N:")
		if new_item == "Y":
			add_item()
	
def delete_item():
	item =  input("What item would you like to delete?")
	quantity = input("How many" + item + "s would you like to delete?")
	del groceries[item]
	
def print_list():
	dictionary = input("Would you like to print your grocery list?")
	print(groceries) 

def finish():
	finish = input("Type: done")
	
def option():
	option = input("What would you like to do? Type add, update, delete, print, or finish: ")
	if option == "add":
		add_item()
		done = True
	elif option == "update":
		update_item()
		done = True
	elif option == "delete":
		delete_item()
		done = True
	elif option == "print":
		print_list() 
		done = True
	else:
		input(done) = True
		return stop 
while not done:
	print(done)
	option()
	
	
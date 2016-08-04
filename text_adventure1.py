start = '''
Congratulations! You're dead. You see a bright light in front of you. Do you go towards it? 
'''
print(start)
done = False
while not done:
    print("Type 'up' to go up or 'down' to go down.")
    user_input = input()
    if user_input == 'up':
        print("Welcome to Hell! You can go left or right.")
        done = True
        print("Type 'left' or 'right'.")
        user_input = input()
        if user_input == 'left':
            print("You are doomed to burn in a pit of flames forever. (You know...Like what usually happens when you go to Hell.)")
            done = True
        elif user_input == 'right':
            print("Nice! You have to listen to bad eighties music for eternity.")
            done = True
        else: 
            print("Please type 'left' or right'")
            user_input = input()
    elif user_input == 'down':
        print("Welcome to Heaven! Would you like to float or walk?")
        done = True
        print("Type 'float' or 'walk'.")
        user_input = input()
        if user_input == 'float':
            print("You don't know how to float. You're a human. You fall down and plummet back to Earth.")
            done = True 
        elif user_input == 'walk':
            print("You meet God and share a meal in the Garden of Eden.")
            done = True
            print("Good job! You won!")
        else: 
            print("Please type 'float' or walk'")
    else:
        print("Please type 'up' or down'")
print("Game Over.") 


	
	

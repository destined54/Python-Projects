enter = '''
Enter your number grade to recieve your letter grade.
'''
print(enter)
user_input = input()
if user_input >= 90:
    print(A)
if user_input >= 80 and user_input < 89:
    print(B)
if user_input >= 70 and user_input < 79:
    print(C)
if user_input >= 0 and user_input < 69:
    print(F)
	 

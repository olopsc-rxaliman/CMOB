# ROVIC XAVIER ALIMAN
# BSCS-2
# February 10, 2024

# 'PRESS ENTER KEY TO CONTINUE...' decorator function
def ask_for_enter_key_after_execution(function):
	def wrapper(*args):
		function(*args)
		input('PRESS ENTER KEY TO CONTINUE...')
		print('')

	return wrapper


Tasklist = []


# Main Menu
def main_menu():
	print('To-do List')
	print('(c) Rovic Aliman 2024\n')

	print('[1] Add task/s')
	print('[2] Remove a task')
	print('[3] Display task/s')
	print('[4] Exit program')

	while True:
		user_input = input(': ')

		if user_input == '1':
			return 'add_task'
		elif user_input == '2':
			return 'remove_task'
		elif user_input == '3':
			return 'display_task'
		elif user_input == '4':
			return 'exit'
		else:
			continue


# Add Task/s
@ask_for_enter_key_after_execution
def add_task():
	print('\nADD TASK/S')
	print('* You may use semicolons (;) to add multiple tasks at once')

	print('\nWhat task/s would you like to add?')

	user_input = input(': ')

	if user_input.replace(';','').strip() == '':
		print('ERROR: You can\'t add an empty task')
	else:
		tasks = user_input.split(';')
		print('\nSuccessfully added the following task/s to the Tasklist:')
		for task in tasks:
			if task == '':
				continue
			else:
				task = task.strip()
				print(f'[] {task}')
				Tasklist.append(task)
	
	print('')


# Remove Task
@ask_for_enter_key_after_execution
def remove_task():
	print('\nREMOVE TASK')

	if Tasklist == []:
		print('There\'s nothing to remove :/')
	else:
		print('What task would you like to remove?')
		user_input = input(': ')
		if user_input == '':
			print('ERROR: You can\'t remove an empty task')
		elif user_input in Tasklist:
			print(f'\nSuccessfully removed "{user_input}" from the Tasklist')
			Tasklist.remove(user_input)
		else:
			print(f'"{user_input}" was not in the Tasklist')

	print('')


# Display Task/s
@ask_for_enter_key_after_execution
def display_task():
	print('\nDISPLAY TASK/S')

	if Tasklist == []:
		print('The Tasklist is empty... You\'re good to go!')
	else:
		print('Here\'s what\'s inside the Tasklist:')
		for task in Tasklist:
			print(f'[] {task}')

	print('')


# Program Entry
while True:
	route = main_menu()

	if route == 'add_task':
		add_task()
	elif route == 'remove_task':
		remove_task()
	elif route == 'display_task':
		display_task()
	elif route == 'exit':
		exit()
	
	continue
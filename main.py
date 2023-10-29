from test_functions import ask_user, ask_computer, determine_winner

# Prompt user to make a choice and print relevant ASCII art
user_choice = ask_user()

# Generate computer's choice and print relevant ASCII art
computer_choice = ask_computer()

# Determine winner
determine_winner(user_choice, computer_choice)

# Exit now the game is over
exit()

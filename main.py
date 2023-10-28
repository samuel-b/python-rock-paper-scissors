import random
import choices_art

# User makes a choice
user_choice = int(input("Do you choose 0 for rock, 1 for paper or 2 for scissors?\n"))

# Exit if the user choice is invalid
if user_choice < 0 or user_choice > 2:
    print("Invalid choice, please choice a number in-between 0 and 2 (inclusive)")
    exit()

# Print users choice
print(f"You chose:\n{choices_art.choice_list[user_choice]}\n")

# Computer generates a random choice
computer_choice = random.randint(0, 2)

# Print computers choice
print(f"Computer chose:\n{choices_art.choice_list[computer_choice]}\n")

# Determine winner
if user_choice == computer_choice:
    print("It's a draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice == 2 and user_choice == 0:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
exit()

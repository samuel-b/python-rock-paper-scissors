import choices_art
import random
import pytest


def ask_user():
    # Prompt user for input, if a valid input cast to integer and print ASCII art, otherwise raise a ValueError
    user_input = input("Do you choose 0 for rock, 1 for paper or 2 for scissors?\n")
    match user_input:
        case "0" | "1" | "2":
            user_input = int(user_input)
            print(f"You chose:\n{choices_art.choice_list[user_input]}\n")
            return user_input
        case _:
            raise ValueError(f"{user_input} is an invalid choice")


def test_ask_user(monkeypatch):
    # If input is a valid choice, confirm an integer of the valid choice is returned
    valid_inputs = ["0", "1", "2"]
    for valid_input in valid_inputs:
        monkeypatch.setattr('builtins.input', lambda _: valid_input)
        assert ask_user() == int(valid_input)

    # If input is an invalid choice, confirm a ValueError is raised
    invalid_inputs = [random.randint(-100, -1), random.randint(3, 100), random.random(), "abc"]
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError):
            monkeypatch.setattr('builtins.input', lambda _: invalid_input)
            ask_user()


def ask_computer():
    # Generate a random integer between 0 and 2 (inclusive) and print ASCII art
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices_art.choice_list[computer_choice]}\n")
    return computer_choice


def test_ask_computer():
    # Confirm an integer is returned between 0 and 2 (inclusive)
    assert type(ask_computer()) == int
    assert 0 <= ask_computer() <= 2


def determine_winner(u_choice, c_choice):
    # Compare the user and computer's choice to determine the winner and return the outcome
    outcome = ""
    if u_choice == c_choice:
        outcome = "draw"
    elif u_choice == 0 and c_choice == 2:
        outcome = "win"
    elif u_choice == 2 and c_choice == 0:
        outcome = "lose"
    elif u_choice < c_choice:
        outcome = "lose"
    elif u_choice > c_choice:
        outcome = "win"

    if outcome == "draw":
        print(f"It's a {outcome}!")
    else:
        print(f"You {outcome}!")
    return outcome


def test_determine_winner():
    # Confirm the correct winner is determined using all combinations
    # Rock vs Rock
    assert determine_winner(0, 0) == "draw"
    # Paper vs Paper
    assert determine_winner(1, 1) == "draw"
    # Scissors vs Scissors
    assert determine_winner(2, 2) == "draw"
    # Rock vs Scissors
    assert determine_winner(0, 2) == "win"
    # Paper vs Rock
    assert determine_winner(1, 0) == "win"
    # Scissors vs Paper
    assert determine_winner(2, 1) == "win"
    # Rock vs Paper
    assert determine_winner(0, 1) == "lose"
    # Paper vs Scissors
    assert determine_winner(1, 2) == "lose"
    # Scissors vs Rock
    assert determine_winner(2, 0) == "lose"

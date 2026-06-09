import random

# Import lesson data
from lessons import consonants, vowels

# Import memory functions
from memory import (
    load_memory,
    add_mistake,
    add_lesson
)


# Start adaptive lesson
def start_lesson():

    memory = load_memory()

    print("\n- Hangul Tutor -")

    # Personalized review section
    if memory["weak_letters"]:

        print("\nYour weak letters:")

        for letter in memory["weak_letters"]:

            # Check consonants
            if letter in consonants:

                print(f"{letter} = {consonants[letter]}")

            # Check vowels
            elif letter in vowels:

                print(f"{letter} = {vowels[letter]}")

    else:

        print("\nNo weak letters yet.")

    # Show lesson content
    print("\nToday's consonants:")

    for letter, sound in consonants.items():

        print(f"{letter} = {sound}")

    # Save lesson history
    add_lesson("Adaptive Hangul Review")


# Quiz system
def quiz_user():

    memory = load_memory()

    # Combine consonants + vowels
    all_letters = {}

    all_letters.update(consonants)
    all_letters.update(vowels)

    # PRIORITIZE weak letters
    if memory["weak_letters"]:

        chosen_letter = random.choice(memory["weak_letters"])

    else:

        chosen_letter = random.choice(list(all_letters.keys()))

    # Correct answer
    correct_answer = all_letters[chosen_letter]

    # Ask user
    answer = input(
        f"\nWhat sound does {chosen_letter} make? "
    )

    # Check answer
    if answer.lower() not in correct_answer.lower():

        print(f"Incorrect.")

        print(f"Correct answer: {correct_answer}")

        add_mistake(chosen_letter)

    else:

        print("Correct!")
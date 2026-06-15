# Import tutor functions
from tutor import (
    start_lesson,
    quiz_user
)

from quiz import (
    conversation_practice
)

# Import conversational system
from conversation import chat


# Startup message
print("Korean Hangul Memory Tutor")


# Main program loop
while True:

    # Menu options
    print("\n1. Start Lesson")
    print("2. Vowel/Constant Quiz")
    print("3. Chat With Tutor")
    print("4. Basic Conversations")
    print("5. Exit")

    # User choice
    choice = input("\nChoose: ")

    # Start lesson
    if choice == "1":

        start_lesson()

    # Start quiz
    elif choice == "2":

        quiz_user()

    # Conversational tutor
    elif choice == "3":

        chat()
    
    # Start Conversation
    elif choice == "4":

        conversation_practice()

    # Exit program
    elif choice == "5":

        print("\nGoodbye!")

        break

    else:

        print("\nInvalid choice.")
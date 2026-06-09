from memory import load_memory


# Simple conversational AI logic
def chat():

    memory = load_memory()

    user_input = input("\nYou: ").lower()

    # User wants weak letters
    if "weak" in user_input:

        print("\nTutor:")

        print("These are your weak letters:")

        print(memory["weak_letters"])

    # User wants vowel practice
    elif "vowel" in user_input:

        print("\nTutor:")

        print("Let's practice vowels today!")

    # User wants consonant practice
    elif "consonant" in user_input:

        print("\nTutor:")

        print("Let's practice consonants!")

    # User asks for progress
    elif "progress" in user_input:

        print("\nTutor:")

        print("Lessons completed:")

        print(memory["previous_lessons"])

    else:

        print("\nTutor:")

        print("I can help you study Hangul!")
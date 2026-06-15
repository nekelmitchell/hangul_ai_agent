from memory import load_memory


from ai_tutor import ask_ai_tutor

def chat():

    memory = load_memory()

    user_input = input("\nYou: ")

    response = ask_ai_tutor(
        user_input,
        memory
    )

    print("\nTutor:")
    print(response)
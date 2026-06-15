import random

from basic_conversations import (
    conversation_scenarios
)

from memory import (
    add_conversation_mistake
)


def conversation_practice():

    scenario = random.choice(
        conversation_scenarios
    )

    print("\n Korean Conversation Practice ")

    print(
        f"\nTutor: {scenario['prompt']}"
    )

    print(
        f"({scenario['translation']})"
    )

    print("\nChoose the best response:\n")

    for i, choice in enumerate(
        scenario["choices"],
        start=1
    ):

        print(f"{i}. {choice}")

    answer = input("\nChoice: ")

    try:

        answer = int(answer)

        if answer == scenario["correct"]:

            print("\nCorrect!")

        else:

            print("\nIncorrect.")

            add_conversation_mistake(
                scenario["prompt"]
            )

        print(
            f"\nExplanation:"
        )

        print(
            scenario["explanation"]
        )

    except ValueError:

        print("Please enter a number.")
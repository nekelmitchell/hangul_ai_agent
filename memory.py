import json
import os

# Memory storage file
MEMORY_FILE = "student_memory.json"

def add_conversation_mistake(prompt):

    memory = load_memory()

    memory["conversation_mistakes"].append(prompt)

    save_memory(memory)

# Load memory
def load_memory():

    default_memory = {

        "previous_lessons": [],
        "mistakes": [],
        "bad_habits": [],
        "weak_letters": [],
        "mistake_counts": {}
    }

    # If file does not exist
    if not os.path.exists(MEMORY_FILE):

        return default_memory

    try:

        with open(MEMORY_FILE, "r") as file:

            return json.load(file)

    # If JSON is broken/empty
    except json.JSONDecodeError:

        return default_memory


# Save memory
def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:

        json.dump(memory, file, indent=4)


# Store mistake
def add_mistake(letter):

    memory = load_memory()

    # Add to mistakes list
    memory["mistakes"].append(letter)

    # Add weak letter if not already stored
    if letter not in memory["weak_letters"]:

        memory["weak_letters"].append(letter)

    # Count mistakes
    if letter not in memory["mistake_counts"]:

        memory["mistake_counts"][letter] = 1

    else:

        memory["mistake_counts"][letter] += 1

    # Detect repeated bad habits
    if memory["mistake_counts"][letter] >= 3:

        if letter not in memory["bad_habits"]:

            memory["bad_habits"].append(letter)

    save_memory(memory)


# Store completed lesson
def add_lesson(topic):

    memory = load_memory()

    memory["previous_lessons"].append(topic)

    save_memory(memory)

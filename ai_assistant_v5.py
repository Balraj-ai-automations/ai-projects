import os
import datetime
import random

memory = {}

print("AI Assistant v5 started")
print("Type 'help' for commands")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("AI Assistant: Goodbye!")
        break

    elif user_input.lower() == "help":
        print("""
Commands:
help   - show commands
clear  - clear screen
exit   - close assistant
time   - show current time
random - generate random number
""")

    elif user_input.lower() == "clear":
        os.system("cls")

    elif user_input.lower() == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"AI Assistant: Current time is {current_time}")

    elif user_input.lower() == "random":
        number = random.randint(1, 100)
        print(f"AI Assistant: Your random number is {number}")

    elif "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip()
        memory["name"] = name
        print(f"AI Assistant: Nice to meet you {name}")

    elif "what is my name" in user_input.lower():
        if "name" in memory:
            print(f"AI Assistant: Your name is {memory['name']}")
        else:
            print("AI Assistant: I don't know your name yet.")

    elif "+" in user_input:
        try:
            parts = user_input.split("+")
            result = int(parts[0]) + int(parts[1])
            print(f"AI Assistant: The answer is {result}")
        except:
            print("AI Assistant: I couldn't calculate that.")

    else:
        print("AI Assistant: I'm still learning.")
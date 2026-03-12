import os

memory = {}

print("AI Assistant v4 started")
print("Type 'help' for commands")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("AI Assistant: Goodbye!")
        break

    elif user_input.lower() == "help":
        print("""
Commands:
help  - show commands
clear - clear screen
exit  - close assistant
""")

    elif user_input.lower() == "clear":
        os.system("cls")

    elif "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip()
        memory["name"] = name
        print(f"AI Assistant: Nice to meet you {name}")

    elif "what is my name" in user_input.lower():
        if "name" in memory:
            print(f"AI Assistant: Your name is {memory['name']}")
        else:
            print("AI Assistant: I don't know your name yet.")

    elif "hello" in user_input.lower():
        print("AI Assistant: Hello! How can I help you?")

    elif "ai" in user_input.lower():
        print("AI Assistant: AI stands for Artificial Intelligence.")

    else:
        print("AI Assistant: I'm still learning.")
import os

print("AI Assistant v3 started")
print("Type 'help' to see commands")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("AI Assistant: Goodbye!")
        break

    elif user_input.lower() == "help":
        print("""
Available commands:
help  - show commands
clear - clear screen
exit  - close assistant
""")

    elif user_input.lower() == "clear":
        os.system("cls")

    elif "ai" in user_input.lower():
        print("AI Assistant: AI stands for Artificial Intelligence. It allows machines to simulate human intelligence.")

    elif "automation" in user_input.lower():
        print("AI Assistant: Automation means using technology to perform tasks automatically.")

    elif "hello" in user_input.lower():
        print("AI Assistant: Hello! How can I help you today?")

    else:
        print("AI Assistant: I'm still learning. Try asking about AI or automation.")
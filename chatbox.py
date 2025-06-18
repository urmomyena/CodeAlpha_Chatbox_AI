print("🤖 ChatBot: Hey! I'm ChatBot. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("🤖 ChatBot: Bye! Have a great day 💖")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("🤖 ChatBot: Hello there!")
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm just code, but I'm doing great 😄")
    elif "name" in user_input:
        print("🤖 ChatBot: I'm just a basic ChatBot created by you!")
    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")

def chatbot():
    print("=========================================================================")
    print("|                      AI RULE-BASED CHATBOT                            |")
    print("=========================================================================\n")
    print("Hello! I am your AI chatbot.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")

    while True:
        user_input: str = input("\nYou: ").lower().strip()

        #Exit commands
        if user_input == "bye" or user_input == "exit" or user_input == "quit":
            print("Bot: Goodbye! Have a great day!")
            break

        #Greetings commands
        elif user_input == "hello" or user_input == "hi" or user_input == "hey":
            print("Bot: Hello!")

        #commands
        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")


        elif user_input == "what is your name":
            print("Bot: My name is RuleBot.")

        elif user_input == "what can you do":
            print("Bot: I can respond to simple predefined messages.")

        #Help command
        elif user_input == "help":
            print("Bot: You can say hello, ask my name, ask how I am, or type bye to exit.")

        #Unknown input
        else:
            print("Bot: I'm sorry, I don't understand that yet.")


# Start the chatbot
chatbot()
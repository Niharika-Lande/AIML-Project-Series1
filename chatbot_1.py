# Define a dictionary of predefined responses
responses = {
    "hello":"Hello!How can i help you?.",
    "hi":"Hi there! How can i assist you.",
    "what is the capital of france?":"the capital of france is paris.",
    " who was the first person to walk on the moon?":"neil armstrong was the first person to walk on the moon during the Apollo 11 mission on July 20, 1969.",
    " how many days are there in a week?": "there are seven days in a week.",
    "How are you doing?":"I'm doing well, thank you for asking!",
    "bye": "Goodbye! Have a great day!",
}

# Define a function to get the bot's response
def get_response(user_input):
    # Convert the input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()
    
    # Find the response in the predefined dictionary
    return responses.get(user_input, "I'm sorry, I don't understand that.")

# Main chat loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        
        # Get the bot's response and print it
        response = get_response(user_input)
        print("Chatbot: " + response)

# Run the chatbot
if __name__ == "__main__":
    chat()

import random

def get_response(user_input):
    # Define the bot's responses based on user input patterns
    if user_input.lower() == "hello":
        return "Hi there!"
    elif user_input.lower() == "how are you?":
        return "I'm good, thanks for asking!"
    elif user_input.lower() == "what can you do?":
        return "I can provide information, answer questions, or just have a casual conversation!"
    elif user_input.lower() == "tell me a joke":
        return "Sure! Here's one: Why don't scientists trust atoms? Because they make up everything!"
    elif user_input.lower() == "flip a coin":
        return random.choice(["Heads!", "Tails!"])
    elif user_input.lower() == "roll a die":
        return "You rolled a " + str(random.randint(1, 6))
    elif user_input.lower() == "who created you?":
        return "I was created by OpenAI."
    elif user_input.lower() == "what is the capital of France?":
        return "The capital of France is Paris."
    elif user_input.lower() == "what is the tallest mountain in the world?":
        return "Mount Everest is the tallest mountain in the world."
    elif user_input.lower() == "tell me an interesting fact":
        facts = [
            "The honeybee is the only insect that produces food eaten by humans.",
            "The Great Wall of China is visible from space.",
            "The average person spends six months of their lifetime waiting for red lights to turn green."
        ]
        return random.choice(facts)
    elif user_input.lower() == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand."

def main():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break

if __name__ == '__main__':
    main()

class Chatbot:
    def __init__(self):
        # Predefined responses
        self.responses = {
            "hours": "Our business hours are 9 AM to 5 PM, Monday to Friday.",
            "location": "We are located at 1234 Elm Street, Springfield.",
            "products": "We sell electronics, furniture, and home appliances.",
            "support": "For support, please call us at 1-800-123-4567 or email support@company.com.",
            "goodbye": "Thank you for chatting with us! Have a great day!",
            "default": "I'm sorry, I don't understand that. Can you please rephrase your question?"
        }

    def handle_user_input(self, user_input):
        # Convert input to lowercase for case-insensitive matching
        lower_input = user_input.lower()
        if lower_input in self.responses:
            print(self.responses[lower_input])
        else:
            print(self.responses["default"])

    def start_conversation(self):
        print("Welcome to our customer service chat! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "goodbye":
                print(self.responses["goodbye"])
                break
            self.handle_user_input(user_input)

def main():
    chatbot = Chatbot()
    chatbot.start_conversation()

if __name__ == "__main__":
    main()

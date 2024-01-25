class Admissionbot:
    def __init__(self):
        self.context = {}

    def respond(self, user_input):
        # Handle user input and provide responses
        response = ""

        if "deadline" in user_input:
            response = "The application deadline is on 25/08/2024."
        elif "requirements" in user_input:
            response = "To apply, you need to fill out the form available on our website and visit our college once after the admission is approved."
        elif "procedure" in user_input:
            response = "The admission procedure involves the student's credentials and xerox copies of their X, XI, XII - Certificates."
        else:
            response = "I'm sorry, I couldn't understand your query. Please ask something else."

        return response

    def chat(self):
        print("Admissionbot: Hi! How can I help you with our college admission?")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == "exit":
                print("Admissionbot: Goodbye! If you have more questions, feel free to ask later.")
                break
            
            response = self.respond(user_input)
            print("Admissionbot:", response)

# Instantiate and run the chatbot
admission_bot = Admissionbot()
admission_bot.chat()

import random
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)


def speak(text):
    print("🤖:", text)
    
    engine.stop()              # stop previous speech
    engine.say(text)
    engine.runAndWait()        # wait until finished
    time.sleep(0.3)            # small delay (IMPORTANT)

# dictionary
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "your name": ["I am PyBot.", "I am your assistant."],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "help": ["I can chat and solve calculations!", "Try typing 2+3"]
}

# function for Calculator
def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Invalid calculation"

 
def chatbot():
    speak("Hello! I am your chatbot. Type exit to quit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            speak("Goodbye!")
            break
        
        if any(op in user_input for op in ['+', '-', '*', '/', '%']):
            speak("Result is " + calculate(user_input))
            continue
        
       
        found = False
        
        for key in responses:
            if key in user_input:
                speak(random.choice(responses[key]))
                found = True
                break
        
        if not found:
            speak("Sorry, I don't understand that.")


chatbot()
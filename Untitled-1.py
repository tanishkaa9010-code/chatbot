import random
user_name = ""

def speak(text):
    print("Pybot:", text)
    
    try:
        import pyttsx3
        engine = pyttsx3.init()  
        
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) 
        
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        
    except Exception as e:
        print("Voice error:", e)

greetings = ["Hi there!", "Hello!", "Hey!"]
status = ["I'm fine!", "Doing great!", "All good!"]
name_resp = ["I am PyBot.", "I am your assistant. What is your name?"]
bye_resp = ["Goodbye!", "See you later!", "Bye!"]
help_resp = ["I can chat and solve calculations!", "Try typing 2+3"]

# Dictionary
responses = {
    "hello": greetings,
    "hi": greetings,
    "hey": greetings,
    "how": status,
    "name": name_resp,
    "bye": bye_resp,
    "help": help_resp
}

def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Invalid calculation"

def chatbot():
    global user_name
    
    speak("Hello! I am your chatbot. Type exit to quit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            speak(f"Goodbye {user_name}!" if user_name else "Goodbye!")
            break
        
        # Calculator
        if any(op in user_input for op in ['+', '-', '*', '/', '%']):
            speak("Result is " + calculate(user_input))
            continue
        
        
        if "your name" in user_input:
            speak("I am PyBot. What is your name?")
            user_name = input("Enter your name: ")
            speak(f"Nice to meet you {user_name}!")
            continue
        
       
        if "how are you" in user_input:
            if user_name:
                speak(f"I am fine, {user_name}!")
            else:
                speak("I am fine!")
            continue
        
       
        words = user_input.split()
        
        found = False
        
        for key in responses:
            if key in words:
                if user_name:
                    speak(f"{random.choice(responses[key])} {user_name}")
                else:
                    speak(random.choice(responses[key]))
                found = True
                break
        
        if not found:
            speak("Sorry, I don't understand that.")
chatbot()
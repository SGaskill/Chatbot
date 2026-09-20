#Create a chatbot program that runs in the Python console (command line).



print("Hello User, I'm chatbot. Call me Botty.")

#What is your name? with terminate program option to end the program if the user types "exit" etc. 

while True:
    name = input("What is your name? (or type 'exit' to leave): ")
    if name.lower() in ["exit", "quit", "bye", "goodbye", "see you", "see ya", "later", "farewell", "adios", "ciao", "sayonara", "peace out", "leave"]:
        print("Goodbye! It was nice chatting with you. Have a great day!")
        import sys
        sys.exit()
    elif name.strip() == "":
        print("Please enter a valid name.")
        continue
    else:
        print(f"Nice to meet you, {name}!")
        break

#Data storage: Keep the user’s name in a variable. (Optional: Save it in a text file to remember after restart.)
with open("username.txt", "w") as file:
    file.write(name)

#How are you?
while True:
    mood = input("How are you? ")
    mood = mood.lower()
    if mood in ["okay", "ok", "good", "great", "fine", "well", "awesome", "amazing", "fantastic", "doing well", "i'm good", "i'm great", "i'm fine", "i'm awesome", "i'm amazing", "i'm fantastic"]:
        print("That's great to hear!")
        break
    elif mood in ["bad", "sad", "not good", "terrible", "awful", "horrible", "unhappy", "depressed", "I'm sad", "I'm bad", "I'm not good", "I'm terrible", "I'm awful", "I'm horrible", "I'm unhappy", "I'm depressed"]:
        print("I'm sorry to hear that. I hope things get better soon.")
        break
    else:
        print("I'm sorry, I can't understand what you said. Try again.")

#What's the time? 12 hour format
while True:
    time_response = input("Would you like to know the current time? (yes/no) ")
    if time_response.lower() in ["yes", "Yes", "y", "sure", "okay", "why not"]:
        import datetime
        now = datetime.datetime.now()
        print("The current time is: ")
        print(now.strftime("%d/%m/%Y \n%I:%M %p"))
        break
    elif time_response.lower() in ["no", "No", "n", "not now", "maybe later"]:
        print("No worries! Maybe next time.")
        break
    else:
        print("Please answer with 'yes' or 'no'.")

#Tell a joke
import random
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "What do you call a bear with no teeth? A gummy bear!"
]
print("Would you like to hear a joke? (yes/no)")
while True:
        joke_response = input().lower()
        if joke_response in ["yes", "Yes", "y", "sure", "okay", "why not"]:
            print(random.choice(jokes))
            break
        elif joke_response in ["no", "No", "n", "not now", "maybe later"]:
            print("No worries! Maybe next time.")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

#Goodbye
while True:
        exit_response = input("Would you like to exit the chat? (yes/no): ").lower()
        if exit_response in ["yes", "y", "exit", "quit"]:
            print(f"Goodbye {name}! It was nice chatting with you. Have a great day!")
            import sys
            sys.exit()
        elif exit_response in ["no", "n", "stay", "continue"]:
            print("Great! Let's contine chatting.")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

#What can you do (help command)
while True:
        help_response = input("Do you want to know more about me or do you want to continue: ").lower()
        if help_response in ["yes", "sure", "y", "help", "info", "information", "i want to know", "help" "what can you do", "what are your functions", "what are your features", "what can you assist with", "what can you help with", "tell me more about you", "more info", "more information"]:
            print("I can do the following things:")
            print("1. Ask for your name.")
            print("2. How you are doing.")
            print("3. Tell you the time.")
            print("4. Tell you a joke.")
            print("5. provide help.")
            print("6. Repeat after you.")
            print("7. Remember your name.")
            print("8. Tell you your name.")
            break
        elif help_response in ["no", "next", "n", "continue", "c", "proceed", "go on", "move on", "skip", "skip this", "no thanks", "no thank you", "no need", "no help", "no assistance", "no info", "no information"]:
            print("Alright, let's continue.")
            break
        else:
            print("I'm sorry, I don't understand that command. Please ask for help or type 'continue' to proceed.")
    

#Repeat after me
while True:
        repeat_response = input("Type something and I'll repeat it back to you (or type 'exit' to leave): ")
        if repeat_response.lower() in ["exit", "quit"]:
            print(f"Goodbye {name}! It was nice chatting with you. Have a great day!")
            import sys
            sys.exit()
        elif print(f"You said: {repeat_response}"):
            break
        else:
            print("I'm sorry, I didn't catch that. Please try again.")
        
        

#Remember my name is [name] (Bring back the name if the user asks "What's my name?" from the txt file)
while True:
        remember_response = input("I can remember your name. Would you like me to tell you? Or you can leave: ")
        if remember_response.lower() in ["exit", "bye", "leave", "quit", "goodbye", "see you", "see ya", "later", "farewell", "adios", "ciao", "sayonara", "peace out"]:
            print(f"Goodbye {name}! It was nice chatting with you. Have a great day!")
            import sys
            sys.exit()
        elif remember_response.lower() in ["yes", "y", "sure", "okay", "why not", "tell me", "do it", "go ahead", "please", "yeah", "yep", "affirmative"]:
            with open("username.txt", "r") as file:
                name = file.read()
            print(f"Great! I will remember that your name is {name}.")
            break
        elif remember_response.lower() in ["no", "n", "not now", "maybe later"]:
            print("No problemo! Maybe next time.")
            break
        else:
            print("I'm sorry, I don't understand what you said. Please ask if you want me to remember your name or type 'exit' to leave.")

#What's my name?
while True:
        name_response = input("You can ask me to tell you your name. Would you like me to say it? (or type 'exit' to leave): ")
        if name_response.lower() in ["exit", "quit", "bye", "goodbye", "see you", "see ya", "later", "farewell", "adios", "ciao", "sayonara", "peace out", "leave"]:
            print(f"Goodbye {name}! It was nice chatting with you. Have a great day!")
            import sys
            sys.exit()
        elif name_response.lower() in ["yes", "y", "sure", "okay", "why not", "tell me", "do it", "go ahead", "please", "yeah", "yep", "affirmative", "what's my name?", "what is my name?", "can you tell me my name?", "do you remember my name?", "remind me my name"]:
            print(f"Your name is {name}.")
            continue
        else:
            print("I'm sorry, I don't what you said. Please ask if you want me to tell you your name or type 'exit' to leave.")

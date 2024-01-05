import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Manthan")

    while True:
        x = input("Enter what you want me to pronounce (type 'q' to quit): ")

        if x.lower() == "q":
            print("Bye Bye my Friend")
            break

        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()

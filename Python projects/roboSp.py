import pyttsx3

if __name__ == '__main__':
    print('welcome to the roboSpeaker')
    s = input("hello are you")
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Say the input text
    engine.say(s)
    
    # Wait for the speech to finish
    engine.runAndWait()

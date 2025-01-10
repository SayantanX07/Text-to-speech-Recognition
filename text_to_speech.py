import pyttsx3
def speech(text):
    python=pyttsx3.init()
    python.say(text)
    python.runAndWait()
def main():
    name=input("enter your name: ")
    text=f"Hello, {name} how are you doing?"
    print(text)
    speech(text)
__name__== "main"
main()

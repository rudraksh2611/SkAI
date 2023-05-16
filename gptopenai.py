import openai
import speech_recognition as sr
import pyttsx3
import os
import pyaudio
import datetime
#import Pygame # for animated video (Work in progress)

# Set up OpenAI credentials
openai.api_key = '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'

# Set up text-to-speech engine
engine = pyttsx3.init('sapi5')

# Define Function to wish me 
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!Rudraksh sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Rudraksh sir") 

    else:
        speak("Good Evening!Rudraksh sir") 

    speak ("My name is skai. Please tell me how may i help you")

# Define function to get text input from speech
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: ", text)
            return text
        except:
            print("Sorry, could not understand audio input.")
            return ""

# Define function to generate OpenAI response
def generate_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2049,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

# Define function to speak response
def speak(text):
        engine.say(text)
        engine.runAndWait()

    # Main loop
if __name__=='__main__':
    wishme()
while True:
        # Get voice input from user
        user_input = get_voice_input()
        # Generate OpenAI response based on user input
        prompt = f"user: {user_input}\nAI:"
        ai_response = generate_openai_response(prompt)
        # Print and Speak OpenAI response
        print(ai_response)
        speak(ai_response)
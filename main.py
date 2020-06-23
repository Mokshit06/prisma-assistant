import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import time
import os
import re
import ssl
import certifi
from pyautogui import screenshot
# import pathlib


class Person:
    name = ''

    def set_name(self, name):
        self.name = name


class Assistant:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak(
                f'Sorry, I didn\'t get that.\nTry saying:-\n   · What time is it?\n   · Where is Delhi?\n')
        except sr.RequestError:
            speak(
                'Sorry, I cant connect to my servers. Try again later.')
        print(f'Q: {voice_data}')
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    file_num = random.randint(1, 20000000)
    audio_file = f'audio-{file_num}.mp3'
    tts.save(audio_file)
    print(f'>> {audio_string}\n')
    playsound.playsound(audio_file)
    os.remove(audio_file)


def there_is(terms):
    for term in terms:
        if re.search(r'\b' + re.escape(term) + r'\b', voice_data.lower()):
            return True


def respond(voice_data):
    if there_is(['hi', 'hello', 'hey']):
        greetings = [f'Hey, how can I help you {person.name}', f'Hi {person.name}! May I help you?',
                     f'Hey, what\'s up {person.name}', f'Hello {person.name}', 'Hey there, how can I help?']

        greeting = greetings[random.randint(0, len(greetings) - 1)]
        speak(greeting)

    if there_is(['my name is']):
        name = voice_data.split('is')[-1].strip()
        person.set_name(name)
        speak(f'Okay, I\'ll remember that {name}')

    if there_is(['what is your name', 'who are you', 'tell me your name']):
        terms = [f'My name is {assistant.name}', 'What\'s up with my name',
                 f'My name is {assistant.name}, hey!', f'The name\'s Assistant. {assistant.name} Assistant']
        term = terms[random.randint(0, len(terms) - 1)]
        speak(term)

    if there_is(['your name should be']):
        name = voice_data.split('be')[-1].strip()
        assistant.set_name(name)
        speak(f'Okat I\'ll remember my new name {person.name}')

    if there_is(['what time is it', 'what is the time', 'tell me the time']):
        time = ctime().split(' ')[3].split(':')[0:2]
        if time[0] == '00':
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'The time is {hours}:{minutes}'
        speak(time)

    if there_is(['how are you', 'how are you doing']):
        speak(f'I\'m very well, thanks for asking {person.name}')

    if there_is(['search for', 'look for']) and 'youtube' not in voice_data:
        search_term = voice_data.split('for')[-1].strip()
        url = f'https://google.com/search?q={search_term}'
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_is(['definition of']):
        search_term = voice_data.split('of')[-1].strip()
        url = f'https://en.wikipedia.org/wiki/{search_term}'
        webbrowser.get().open(url)
        speak(f'Here is what I found about {search_term} on wikipedia')

    if there_is(['youtube']):
        search_term = voice_data.split('for')[-1].strip()
        url = f'https://youtube.com/results?search_query={search_term}'
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term}')

    if there_is(['price of']):
        search_term = voice_data.split('of')[-1].strip()
        url = f'https://amazon.com/s?k={search_term}'
        webbrowser.get().open(url)
        speak(f'Check what I found for {search_term}')

    if there_is(['capture', 'screenshot', 'my screen']):
        screenshot_captured = screenshot()
        file_num = random.randint(1, 10000)
        destination = f'screen-{file_num}.png'
        screenshot_captured.save(destination)
        speak(f'Screenshot is saved at {destination}')

    if there_is(['game']):
        user_move = record_audio('Choose your move')
        computer_choices = ['rock', 'paper', 'scissors']

        computer_move = computer_choices[random.randint(
            0, len(computer_choices) - 1)]

        speak(f'The computer chose {computer_move}.\nYou chose {user_move}')
        if computer_move == user_move:
            speak('The match is draw')
        elif user_move == 'rock':
            if computer_move == 'paper':
                speak('Congrats! You won')
            else:
                speak('Computer won')
        elif user_move == 'paper':
            if computer_move == 'rock':
                speak('Congrats! You won')
            else:
                speak('Computer won')
        elif user_move == 'scissors':
            if computer_move == 'rock':
                speak('Congrats! You won')
            else:
                speak('Computer won')
        else:
            speak('Please choose a move')

    if there_is(['plus', 'minus', 'divide', 'multiply', 'power', '+', '-', '*', '/']):
        expression = voice_data.split()[1]

        if expression == '+':
            speak(
                int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif expression == '-':
            speak(
                int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif expression == 'multiply':
            speak(
                int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif expression == 'divide':
            speak(
                int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif expression == 'power':
            speak(
                int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            speak("Wrong Expression")

    if there_is(['location of', 'where is']):
        location = voice_data.split('of')[-1].strip() if len(
            voice_data.split('is')) == 1 else voice_data.split('is')[-1].strip()
        url = f'https://google.com/maps/place/{location}/&amp'
        webbrowser.get().open(url)
        speak(f'Here is the location of {location}')

    if there_is(['exit', 'bye', 'goodbye', 'quit']):
        speak(f'Goodbye {person.name}')
        exit()


time.sleep(1)

person = Person()
assistant = Assistant('Prisma')
print('\n')
speak('Try saying something!')

while True:
    voice_data = record_audio()
    respond(voice_data)

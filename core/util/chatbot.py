import aiml
import sys
import os
import pyttsx3
from pyttsx3 import driver
import speech_recognition as sr

class ChatBot():  
        
    def falar(frase):          
        engine=pyttsx3.init()# criação de objeto  
        engine.setProperty ('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_ptBR_DanielM")     
        engine.setProperty('rate', 200)       
        print(">>bot: " )               
        engine.say(frase) 
        engine.runAndWait()      

    #Função para fazer o bot ouvir.
    def ouvir():
        #habilita o microfone para ouvir o usuario
        recognizer=sr.Recognizer()
        microfone=sr.Microphone()
        # função para redução de ruido
        with microfone as source:
            
            recognizer.adjust_for_ambient_noise(source, duration=0.5)           
            print(">>Humano:")
            #Armazena a informação do audio na variavel    
            audio=recognizer.listen(source)
            
        try:
            recognizer.recognize_google(audio, show_all=True)
            frase=recognizer.recognize_google(audio, language="pt-br")
            print("você disse:" + frase)
            return frase
        except sr.UnknownValueError:
            return ""
            

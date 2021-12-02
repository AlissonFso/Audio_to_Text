from subprocess import run
from tkinter import * 
from tkinter import messagebox
import tkinter
import speech_recognition as sr
import pyperclip
from time import sleep
from threading import Thread
from threading import Timer





class MinhaGUI:

    def __init__(self):
        
        self.janela_principal = Tk()
        self.janela_principal.geometry('500x500')
  
        
        self.text = tkinter.StringVar()
        self.res = tkinter.StringVar()
        self.text.set("Gravar")
        self.botao = Button(self.janela_principal, textvariable=self.text, command=self.click, font='-weight bold -size 12')
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit, font='-weight bold -size 10')
        self.botao.pack(side="top", fill='both', expand=False, padx=1, pady=1)
        self.botao_sair.pack(side="bottom", fill='both', expand=False, padx=1, pady=1)
  
        
        self.botao.pack()
        self.botao_sair.pack()
        

        self.scroll = Scrollbar(self.janela_principal)
        self.caixa = Text(self.janela_principal, yscrollcommand= self.scroll.set)
        self.scroll.pack(side="right",fill="y",expand=False)
        self.caixa.pack()
        self.scroll.config(command=self.caixa.yview)

        self.label1 = tkinter.Label(self.janela_principal, textvariable= self.res, wraplength=500, font ='-weight bold -size 9' )
        self.label1.pack(side='bottom')


        
        mainloop()

    def start(self):
        """Enable scanning by setting the global flag to True."""
        
        self.running = True

    def stop(self):
        """Stop scanning by setting the global flag to False."""
        
        self.running = False
        self.text.set("Gravar")
        self.botao_parar.destroy()


    def click(self):
        self.start()
        Thread(target = self.text.set("Gravando")).start()
        self.botao_parar = Button(self.janela_principal, text='Parar', command = self.stop , font='-weight bold -size 10')
        self.botao_parar.pack(side="top", fill='both', expand=False, padx=1, pady=1)
        Thread(target = self.gravar).start()
       
        


    def gravar(self):
        global running


        microfone = sr.Recognizer()
        
        with sr.Microphone() as source:
        
            
            microfone.adjust_for_ambient_noise(source, duration=1)
            #microfone.dynamic_energy_threshold = True
            #microfone.energy_threshold = 500000
            #microfone.pause_threshold = 0.8
            #microfone.dynamic_energy_adjustment_ratio = 5
            
            print(" - ")
            audio = microfone.listen(source)

            while self.running == True: 
                try:
            
                    
                    frase = microfone.recognize_google(audio,language='pt-BR')
                    
                    frase_1 = frase.replace('asterisco', '*')
                    
                    frase_2 = frase_1.replace('jogo da velha', '#')
                    frase_ok = frase_2.replace('jogo-da-velha', '#')
                    frase_ok = frase_ok.replace('700 e 1', '701')
                    self.res.set(frase_ok)
                    self.caixa.insert('1.0', frase_ok+'\n')
                    pyperclip.copy(frase_ok)
                    self.text.set("Gravar")
                    self.botao_parar.destroy()
                    self.running = False

            
        
                except:
                    print("Erro!!")
                    #print(frase_ok)
            
        
  


gui = MinhaGUI()
'''
 Before running type:
    --> pip install gTTS 
    --> pip install playsound3
'''
from gtts import gTTS  
from playsound3 import playsound   

text_val = input("Enter the text which you want to convert: ")  
  
language = 'en'  
obj = gTTS(text=text_val, lang=language, slow=False)   
obj.save("python.mp3")  # saves audio file in the existing folder
  
playsound("python.mp3")  # plays the audio when you run the program
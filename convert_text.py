import os
#IMPORT SYS FOR FILE IN COMMAD LINE
import sys

#IMPORT MODULO pip install SpeechRecognition
try:
	import speech_recognition as sr
except Exception as e:
	os.system("pip install SpeechRecognition")
	import speech_recognition as sr


#join file 
def getNameFile():
	num = 0
	while os.path.exists("Convert_audio_text_{0}.txt".format(str(num))):
		num +=1
	return "Convert_audio_text_{0}.txt".format(str(num))
def saveFile(text):
	name = getNameFile()
	with open(name,"w") as file:
		file.write(text)

# get the audio file
FORMATS = ["wav","flac","aiff"]
def findFileAudio():
	for f in FORMATS:
		if os.path.exists("audio.{}".format(f)):
			return "audio.{}".format(f)
	print("Error")
	print("No hay archivos por convertir")
	print("Vuelva a intentarlo o coloque un archivo-\n en la carpeta actual con el nombre de con el nombre de audio,\nFormatos sopostados wav y flac")

if len(sys.argv) > 1:
	audio = sys.argv[1]
else:
	print("Formatos soportados:  ", ', '.join(FORMATS))
	audio = input("Ingrese nombre o uuta del archivo:\n")
	print(audio)
	if audio == None or not None:
		audio = findFileAudio()
		
#Function extract text from audio 
re = sr.Recognizer()

# Convertion AUDIO-TEXT
with sr.AudioFile(audio) as source:
	#Audio information
	info_audio = re.record(source)
	#Convertion text
	text = re.recognize_google(info_audio, language="es_ES")
	saveFile(text)
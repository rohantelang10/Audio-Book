import pyttsx3
import PyPDF2

pdfFileObj = open('For the love of programming.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageno = pdfReader.numPages
temp = ''

for i in range(pageno):
    pageObj = pdfReader.getPage(i)
    temp = temp+ '\n' + pageObj.extractText()

mytext = temp

pdfFileObj.close()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
while True:
    index = input("In which voice, Do you want to Listen Book (Male/ Female)? - ")
    if "male"==index.lower():
        index = 0
        break
    elif "female"==index.lower():
        index = 1
        break
    else:
        print("Please enter Male/Female:")

engine.setProperty('voice', voices[index].id)
engine.say(mytext)
engine.setProperty('rate', 145)
engine.setProperty('volume', 0.9)
engine.runAndWait()
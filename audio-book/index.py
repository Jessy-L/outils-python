import pyttsx3
book = open('book.txt', 'r')
book_text = book.readline()
engine = pyttsx3.init()
engine.say(book_text)
engine.runAndWait()
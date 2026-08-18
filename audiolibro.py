from pypdf import PdfReader
import pyttsx3

reader = PdfReader("Magiacelta.pdf")

texto = ""

for pagina in reader.pages:
    texto += pagina.extract_text() or ""

print("Texto extraído")

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 150)

engine.save_to_file(texto, "audiolibro.mp3")

engine.runAndWait()

print("Audiolibro creado")
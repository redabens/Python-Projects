import winsound
import pyttsx3
from pynput.mouse import Listener, Button
from pynput import mouse
import time

# Variables pour enregistrer le début et la fin des clics
start_time = None
end_time = None

# Dictionnaire des correspondances Morse
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
    '-....-': '-', '-.--.': '(', '-.--.-': ')', '.-..-.': '"', '.----.': "'",
    '---...': ':', '----': ' '
}
def read_interpretation(interpretation):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)  # Réglage de la vitesse de lecture
    engine.say(interpretation)
    engine.runAndWait()

# Fonction pour émettre un bip en fonction de la durée du clic
def emit_variable_beep(duration):
    if 0 < duration < 1:
        frequency = 800
        winsound.Beep(int(frequency), int(duration * 1000))
   
# Variable pour enregistrer les signaux Morse
morse_signal = ''
message = ""
# Fonction pour détecter les clics de souris
def on_click(x, y, button, pressed):
    global start_time, end_time, morse_signal, message
    if button == mouse.Button.left:
       if pressed:
        start_time = time.time()
       else:
        end_time = time.time()
        click_duration = end_time - start_time
        # Fonction pour émettre un bip
        emit_variable_beep(click_duration)
       
        if click_duration < 0.4:  # Clic court : point
            morse_signal += '.'
        elif click_duration >=0.4 and click_duration <1.0:  # Clic prolongé : tiret
            morse_signal += '-'
        if click_duration > 1.0:  # Fin d'un caractère Morse
            interpretation = interpret_morse()
            message += interpretation
            read_interpretation(interpretation)
    elif button == mouse.Button.right:
         read_interpretation(message)
         message = ''
         
# Fonction pour interpréter le signal Morse
def interpret_morse():
    global morse_signal
   
    if morse_signal in morse_dict:
        character = morse_dict[morse_signal]
        print(character, end='', flush=True)
    else:
        print('?', end='', flush=True)
        character = '?'
   
    morse_signal = ''  # Réinitialiser le signal Morse
    return character

# Démarrer l'écoute des clics de souris
with Listener(on_click=on_click) as listener:
    listener.join()
import speech_recognition as sr
from Workspace import *
import os

file_name = 'backup.txt'

def recognizeaudio(return_existing = False, save_current = False): 
    if return_existing and os.path.exists(os.path.join(os.getcwd(), file_name)): 
        with open(file_name, 'r') as backup: 
            line = backup.readline()[: -1]
            return line
    r = sr.Recognizer()
    mic = sr.Microphone()
    try:
        rec = ""
        while(True): 
            with mic as source: 
                print("Please say the equation:")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            rec = str(r.recognize_google(audio))
            print("You said: " + rec)
            reaction = input("Does that look good? [Y/N] ")
            if 'Y' in reaction: 
                break
        if save_current:
            with open(file_name, 'w+') as writer:
                writer.write(rec + "\n")
        return rec
    except Exception as e:
        print(e)
        return None
#"+ x + 1 ^ 2"

def adjust_binomals(string_part): 
    index = 0
    while(index < len(string_part)):
        if(string_part[index] == '^'): 
            x_index = index
            while(string_part[x_index] != '*'): 
                x_index -= 1
            replacement = "(" + string_part[x_index + 1: index] + ")^"
            pot = replacement.index('x')
            if pot != 1: 
                replacement = replacement[:pot] + "*" + replacement[pot:]
            string_part = string_part[:x_index + 1] + replacement + string_part[index + 1:]
            index = x_index + len(replacement)
        index += 1
    return string_part

def convert_audio_to_equation(recognized_text, debug = False):
    recognized_text = recognized_text.replace(" raised to ", "^")
    recognized_text = recognized_text.replace("is equal to", "=")
    recognized_text = recognized_text.replace(" * ", "*")
    recognized_text = recognized_text.replace("X", "x")
    split = recognized_text.index("=")
    part_1 = recognized_text[0: split].strip()
    part_1 = adjust_binomals(part_1)
    part_2 = recognized_text[split + 1: ].strip()
    part_2 = adjust_binomals(part_2)
    combined = part_1 + " - (" + part_2 + ")"
    if debug:
        print("Formatted to: " + combined)
    expression_solver(combined, debugging = debug)

if __name__ == '__main__':
    #example_input = "1 + 4X raised to 2 is equal to 9"
    #convert_audio_to_equation(example_input)
    user_input = recognizeaudio(return_existing = False, save_current= False)
    convert_audio_to_equation(user_input, debug = False)
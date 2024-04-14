from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    
    font_name = input("Ingrese el nombre de la fuente (deje en blanco para aleatorio): ")
    if not font_name:
        font_name = random.choice(fonts)
    elif font_name not in fonts:
        print("Fuente no válida. Fuentes disponibles:")
        for f in fonts:
            print(f)
        return

    figlet.setFont(font=font_name)
    user_text = input("Ingrese el texto: ")
    ascii_art = figlet.renderText(user_text)
    print(ascii_art)

if __name__ == "__main__":
    main()
    
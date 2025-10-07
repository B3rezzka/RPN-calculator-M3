import random
import time

def animate_text(text, delay=0.03, effect_type="typing"): # Text animation, Effects: typing, random_chars
    if effect_type == "typing":
        for char in text:
            print(f"\033[32m{char}\033[0m", end='', flush=True)
            time.sleep(delay)
        print()
    
    elif effect_type == "random_chars":
        chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~"
        result = []
        for char in text:
            result.append(char)
        
        for i in range(10):
            display_text = ""
            for j, char in enumerate(text):
                if char == ' ':
                    display_text += ' '
                else:
                    display_text += random.choice(chars)
            print(f"\033[34m\r{display_text}\033[0m", end='', flush=True) # Show random characters before actual text
            time.sleep(0.1)
        print(f"\r{text}")


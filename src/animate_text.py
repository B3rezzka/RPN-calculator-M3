import time


def animate_text(text, delay=0.03, effect_type="typing"): # Text animation, Effects: typing, random_chars
    if effect_type == "typing":
        for char in text:
            print(f"\033[32m{char}\033[0m", end='', flush=True)
            time.sleep(delay)
        print()

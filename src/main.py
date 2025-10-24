from src.animate_text import animate_text
from src.calc import calc


def main():
    banner = """ 
    ╔═══════════════════════════════╗
    ║    🧮 RPN CALCULATOR 🧮       ║
    ║  Reverse Polish Notation      ║
    ║       By: B3rezzka            ║
    ╚═══════════════════════════════╝
    """  # Animated welcome banner
    animate_text(banner, 0.03, "typing")
    animate_text("Enter your RPN expression:", 0.03, "typing")
    
    user_input = input("👉 ")
    print(calc(user_input))


if __name__ == '__main__':
    main()
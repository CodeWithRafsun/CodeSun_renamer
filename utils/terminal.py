import os
import sys
import time


# Terminal Colors
CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
BOLD = "\033[1m"
WHITE = "\033[0;37m"
NC = "\033[0m"


def clear():
    """Clear terminal screen"""
    os.system("clear" if os.name != "nt" else "cls")


def success(message):
    """Success message"""
    print(f"{GREEN}✓ SUCCESS:{NC} {message}")


def error(message):
    """Error message"""
    print(f"{RED}✕ ERROR:{NC} {message}")


def warning(message):
    """Warning message"""
    print(f"{YELLOW}⚠ WARNING:{NC} {message}")


def info(message):
    """Information message"""
    print(f"{CYAN}ℹ INFO:{NC} {message}")


def loading(message, duration=1):
    """Simple loading animation"""
    print(f"{CYAN}{message}{NC}", end="")

    for _ in range(3):
        time.sleep(duration / 3)
        print(".", end="", flush=True)

    print()


def progress(message, steps=20):
    """Simple progress bar"""

    print(f"\n{CYAN}{message}{NC}")

    for i in range(steps + 1):
        percent = int((i / steps) * 100)

        bar = "█" * i + "░" * (steps - i)

        sys.stdout.write(
            f"\r[{bar}] {percent}%"
        )

        sys.stdout.flush()
        time.sleep(0.05)

    print("\n")


def divider(length=60):
    """UI divider"""
    print(GREEN + "=" * length + NC)


def box(title, lines):
    """Simple TUI box"""

    print(CYAN + "╔" + "═" * 50 + "╗" + NC)
    print(CYAN + f"║ {title:<48} ║" + NC)
    print(CYAN + "╠" + "═" * 50 + "╣" + NC)

    for line in lines:
        print(CYAN + f"║ {line:<48} ║" + NC)

    print(CYAN + "╚" + "═" * 50 + "╝" + NC)


def banner_text(text):
    """Print formatted banner text"""
    print(BOLD + CYAN)
    print(text)
    print(NC)

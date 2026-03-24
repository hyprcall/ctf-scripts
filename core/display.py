# Helper script for handling messages and banner display
import pyfiglet

# Message Class to add flavor to the terminal
class Message:
    types = {
                "info": ("\033[2m", "[*]"),
                "warning": ("\033[33m", "[!]"),
                "error": ("\033[31m", "[X]"),
                "success": ("\033[32m", "[+]"),
    }
    @staticmethod
    def _print(msg_type, message):
        color, prefix = Message.types.get(msg_type, Message.types["info"])
        print(f"{color}{prefix} {message}\033[0m")

# Prints the Banner of the Main Program
def banner():
    art = pyfiglet.figlet_format("bREach", font="slant")
    print(f"\033[38;2;255;0;18m{art}\033[0m")
    print("\033[38;2;179;179;179mv0.0.1 | hyprcall\033[0m")
    print("\033[38;2;73;177;245mGaining Understanding.\033[0m")


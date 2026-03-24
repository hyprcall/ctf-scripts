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

def banner():
    result = pyfiglet.figlet_format("bREach", "Fire Font-k")
    print(result)

# Checks if the module is active, dependencies, and if the required arguments are present
from .display import Message
import shutil

def validate(data):
    if data['active'] == True:
        Message._print("success", "Module is active")
    else:
        Message._print("error", "Module is not active")
        return False
    for tool in data['dependencies']:
        # Check if the tool is installed
        if shutil.which(tool):
            Message._print("success", f"Found tool: {tool}")
        else:
            Message._print("error", f"Tool not found: {tool}")
            return False
    return True


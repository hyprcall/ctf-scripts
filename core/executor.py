# Starts a subprocess of the module that needs to run
import subprocess
from pathlib import Path

def execute(data, remaining):
    # Update this as more languages get added
    runtimes = {
            "bash" : "bash",
            "python": "python3",
            "c": ""
    }
    # Constructs the command
    path = Path("modules") / data['category'] / data['name'] / data['name']
    language = data['language']
    runtime = runtimes.get(language, "")
    runtime_part = [runtime] if runtime else []
    path_part = [str(path)]
    command = runtime_part + path_part + remaining
    subprocess.run(command)


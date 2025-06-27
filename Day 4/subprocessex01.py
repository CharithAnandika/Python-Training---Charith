import subprocess
import sys

import subprocess
import sys

def execute_command(command, capture_output=True, text=True, check=False):
    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=text,
            check=check,
            shell=isinstance(command, str)  # use shell=True if command is a string
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' failed with exit code {e.returncode}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return None
    except FileNotFoundError:
        print(f"Error: Command not found — '{command}'. Make sure it's installed on your system.")
        return None

def main():
    if sys.platform.startswith('win'):
        list_command = "dir"
    else:
        list_command = ["ls", "-1"]

    result = execute_command(list_command)

    if result and result.returncode == 0:
        print("Command executed successfully:")
        print(result.stdout)
    elif result:
        print(f"Command failed with exit code: {result.returncode}")
        print(f"stderr: {result.stderr}")

if __name__ == "__main__":
    main()


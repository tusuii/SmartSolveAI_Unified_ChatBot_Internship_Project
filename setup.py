import subprocess
import sys
file = "requirements.txt"

def install_pkgs():
    try:
        subprocess.check_call(['pip', 'install', '-r', file])
        subprocess.check_call(['python', '-m', 'spacy', 'download', 'en_core_web_md'])
        
        print("All required packages successfully installed.")
        sys.exit()
    except subprocess.CalledProcessError as e:
        print(f"Error installing: {e}")

if __name__ == "__main__":
    install_pkgs()

# How to run this script?
# python setup.py


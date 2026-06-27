import sys
from sb.commands.status import status
from sb.commands.doctor import doctor

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "status":
        status()
    elif cmd == "doctor":
        doctor()
    else:
        print("SmallBlock SDK")
        print("Commands: status, doctor")

if __name__ == "__main__":
    main()

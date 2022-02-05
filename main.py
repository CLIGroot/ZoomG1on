import zoom
import sys
import os

device = os.open("/dev/midi2", os.O_RDWR)

def tuner():
    try:
        os.write(device, bytearray(zoom.tuner[sys.argv[2].lower()]))
        os.system("clear")

        if sys.argv[2].lower() == "on":
            print(f"TUNER: \033[05m\033[92m{sys.argv[2].upper()}\033[0m")

        if sys.argv[2].lower() == "off":
            print(f"TUNER: \033[05m\033[91m{sys.argv[2].upper()}\033[0m")

        os.close(device)

    except IndexError:
        os.system("clear")
        print("\033[93mWarning!\033[0m",
        "Missing Arguments: ON\OFF")
        os.close(device)

cmd = {
    'tuner': tuner
}

try:
    cmd[sys.argv[1]]()

except IndexError:
    os.system("clear")
    print("\033[93m\t\tCOMMANDS\033[0m")
    print("tuner [ON/OFF]")

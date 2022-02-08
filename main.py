import zoom
import sys
import os

device = os.open("/dev/midi2", os.O_RDWR)

def edit_mode():
    try:
        os.write(device, bytearray(zoom.edit_mode[sys.argv[2].lower()]))
        os.system("clear")

        if sys.argv[2].upper() == "ON":
            print(f"EDIT MODE: \033[05m\033[92m{sys.argv[2].upper()}\033[0m")

        if sys.argv[2].upper() == "OFF":
            print(f"EDIT MODE: \033[05m\033[91m{sys.argv[2].upper()}\033[0m")

        os.close(device)

    except IndexError:
        os.system("clear")
        print("\033[93mWarning!\033[0m",
        "Missing Arguments: ON\OFF")
        os.close(device)

    except KeyError:
        os.system("clear")
        print("\033[93mInvalid Argument\033[0m:",
        f"\033[93m{sys.argv[2].upper()}\033[0m is not a valid argument!",
        "Just \033[93mON\033[0m or \033[93mOFF\033[0m!")
        os.close(device)

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

    except KeyError:
        os.system("clear")
        print("\033[93mInvalid Argument\033[0m:",
        f"\033[93m{sys.argv[2].upper()}\033[0m is not a valid argument!",
        "Just \033[93mON\033[0m or \033[93mOFF\033[0m!")
        os.close(device)

def patch():
    def list():
        for patch in zoom.patch:
            print(patch)
            if patch[-1] == "9":
                print("===")

    try:
        if sys.argv[2] == 'list':
            list()
            return

        os.write(device, bytearray(zoom.patch[sys.argv[2].upper()]))
        os.close(device)

    except IndexError:
        os.system("clear")
        print("\033[93mWarning!\033[0m",
        "Missing Arguments: Patch","\n")
        print("patch list for list of patch")
        os.close(device)

    except KeyError:
        os.system("clear")
        print("\033[93mWarning!\033[0m",
        f"Patch: \033[93m{sys.argv[2].upper()}\033[0m path not found.","\n")
        print("patch list for list of patch")
        os.close(device)

cmd = {
    'tuner': tuner,
    'patch': patch,
    'edit': edit_mode
}

cmd[sys.argv[1]]()

#www.github.com/evillero#



import random
import sys
import os

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ASCII_TITLE = f"""
{Colors.OKGREEN}
▗▄▄▄▖▗▖   ▗▄▄▄▖▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖▗▄▄▖     ▗▄▄▄▄▖▗▄▄▄▖▗▄▄▖  ▗▄▖ 
▐▌   ▐▌     █  ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌       ▗▞▘▐▌   ▐▌ ▐▌▐▌ ▐▌
▐▛▀▀▘▐▌     █  ▐▛▀▘ ▐▛▀▘ ▐▛▀▀▘▐▛▀▚▖     ▗▞▘  ▐▛▀▀▘▐▛▀▚▖▐▌ ▐▌
▐▌   ▐▙▄▄▖▗▄█▄▖▐▌   ▐▌   ▐▙▄▄▖▐▌ ▐▌    ▐▙▄▄▄▖▐▙▄▄▖▐▌ ▐▌▝▚▄▞▘
┌┐ ┬ ┬  ┌─┐┬  ┬┬┬  ┬  ┌─┐┬─┐┌─┐
├┴┐└┬┘  ├┤ └┐┌┘││  │  ├┤ ├┬┘│ │
└─┘ ┴   └─┘ └┘ ┴┴─┘┴─┘└─┘┴└─└─┘
{Colors.ENDC}
"""

class Generate:
    ID_TYPES = {
        "1": ("EM4100", 10, 0xFFFFFFFFFF),
        "2": ("HID Prox", 12, 0xFFFFFFFFFFFF),
        "3": ("PAC/Stanley", 8, 0xFFFFFFFF),
        "4": ("H10301", 6, 0xFFFFFF),
        "5": ("IoProx XSF", 8, 0xFFFFFFFF),
        "6": ("Paradox", 12, 0xFFFFFFFFFFFF),
        "7": ("Indala 26-bit", 6, 0xFFFFFF),
        "8": ("Viking", 8, 0xFFFFFFFF),
        "9": ("Pyramid", 8, 0xFFFFFFFF),
        "10": ("Keri", 8, 0xFFFFFFFF),
        "11": ("Jablotron", 12, 0xFFFFFFFFFFFF),
        "12": ("Electra", 16, 0xFFFFFFFFFFFFFFFF),
        "13": ("IDTECK", 16, 0xFFFFFFFFFFFFFFFF),
        "14": ("Gallagher", 16, 0xFFFFFFFFFFFFFFFF),
        "15": ("Nexwatch", 16, 0xFFFFFFFFFFFFFFFF)
    }

    def generate_ids(self, id_type, output_file, num_ids):
        if id_type not in self.ID_TYPES:
            print(f"{Colors.FAIL}Invalid ID type selected.{Colors.ENDC}")
            return

        name, id_length, id_max = self.ID_TYPES[id_type]
        print(f"{Colors.OKCYAN}Generating {num_ids} {name} IDs...{Colors.ENDC}")

        try:
            with open(output_file, 'w') as file:
                for i in range(num_ids):
                    card_id = random.randint(0, id_max)
                    card_id_str = f"{card_id:0{id_length}X}"
                    file.write(card_id_str + '\n')
                    if (i + 1) % 10000 == 0:
                        print(f"{Colors.OKBLUE}{i + 1} IDs generated...{Colors.ENDC}")
            print(f"{Colors.OKGREEN}Dictionary successfully generated and saved to '{output_file}'.{Colors.ENDC}")
        except IOError as e:
            print(f"{Colors.FAIL}Error writing to file: {e}{Colors.ENDC}")
            sys.exit(1)


if __name__ == '__main__':
    fuzzer = Generate()
    print(f"{Colors.HEADER}{Colors.BOLD}Flipper Zero RFID Fuzzer Generator{Colors.ENDC}")
    print(f"{Colors.OKCYAN}---------------------------------------------{Colors.ENDC}")

    while True:
        print(f"{Colors.BOLD}Select the type of ID to generate:{Colors.ENDC}")
        for key, (name, _, _) in Generate.ID_TYPES.items():
            print(f"{key}. {name}")

        choice = input(f"{Colors.BOLD}Enter your choice (1-15): {Colors.ENDC}").strip()

        if choice in Generate.ID_TYPES:
            num_ids = input(f"{Colors.BOLD}Enter the number of IDs to generate (default: 100,000): {Colors.ENDC}").strip()
            num_ids = int(num_ids) if num_ids.isdigit() and int(num_ids) > 0 else 100000

            output_file = input(f"{Colors.BOLD}Enter the name of the output file (default: 'dictionary.txt'): {Colors.ENDC}").strip()
            if not output_file:
                output_file = 'dictionary.txt'
            elif not output_file.endswith('.txt'):
                output_file += '.txt'

            script_directory = os.path.dirname(os.path.abspath(__file__))
            output_file_path = os.path.join(script_directory, output_file)
            fuzzer.generate_ids(choice, output_file_path, num_ids)
            break
        else:
            print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")

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

def generate_em4100_dictionary(output_file, num_ids):
    try:
        print(f"{Colors.OKCYAN}Generating {num_ids} EM4100 IDs...{Colors.ENDC}")
        with open(output_file, 'w') as file:
            for i in range(num_ids):
                card_id = random.randint(0, 0xFFFFFFFFFF)
                card_id_str = f"{card_id:010X}"
                file.write(card_id_str + '\n')
                if (i + 1) % 10000 == 0:
                    print(f"{Colors.OKBLUE}{i + 1} IDs generated...{Colors.ENDC}")
        print(f"{Colors.OKGREEN}EM4100 dictionary successfully generated and saved to '{output_file}'.{Colors.ENDC}")
    except IOError as e:
        print(f"{Colors.FAIL}Error writing to file: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == '__main__':

    print(ASCII_TITLE)
    print(f"{Colors.HEADER}{Colors.BOLD}Flipper Zero RFID Fuzzer Generator{Colors.ENDC}")
    print(f"{Colors.OKCYAN}---------------------------------------------{Colors.ENDC}")

    while True:
        try:
            num_ids_input = input(
                f"{Colors.BOLD}Enter the number of EM4100 IDs to generate (default: 100,000): {Colors.ENDC}"
            ).strip()
            if num_ids_input == '':
                num_ids = 100000
                break
            else:
                num_ids = int(num_ids_input)
                if num_ids <= 0:
                    print(f"{Colors.WARNING}Please enter a positive integer.{Colors.ENDC}")
                    continue
                break
        except ValueError:
            print(f"{Colors.FAIL}Invalid input. Please enter a valid number.{Colors.ENDC}")

    output_file = input(
        f"{Colors.BOLD}Enter the name of the output file (default: 'em4100_dictionary.txt'): {Colors.ENDC}"
    ).strip()
    if not output_file:
        output_file = 'em4100_dictionary.txt'

    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_directory, output_file)

    generate_em4100_dictionary(output_file_path, num_ids)

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
    print(f"{Colors.OKCYAN}Generating {num_ids} EM4100 IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 10, 0xFFFFFFFFFF)

def generate_hidprox_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} HID Prox IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 12, 0xFFFFFFFFFFFF)

def generate_pac_stanley_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} PAC/Stanley IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 8, 0xFFFFFFFF)

def generate_h10301_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} H10301 IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 6, 0xFFFFFF)

def generate_ioprox_xsf_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} IoProx XSF IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 8, 0xFFFFFFFF)

def generate_paradox_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Paradox IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 12, 0xFFFFFFFFFFFF)

def generate_indala26_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Indala 26-bit IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 6, 0xFFFFFF)

def generate_viking_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Viking IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 8, 0xFFFFFFFF)

def generate_pyramid_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Pyramid IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 8, 0xFFFFFFFF)

def generate_keri_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Keri IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 8, 0xFFFFFFFF)

def generate_jablotron_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Jablotron IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 12, 0xFFFFFFFFFFFF)

def generate_electra_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Electra IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 16, 0xFFFFFFFFFFFFFFFF)

def generate_idteck_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} IDTECK IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 16, 0xFFFFFFFFFFFFFFFF)

def generate_gallagher_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Gallagher IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 16, 0xFFFFFFFFFFFFFFFF)

def generate_nexwatch_dictionary(output_file, num_ids):
    print(f"{Colors.OKCYAN}Generating {num_ids} Nexwatch IDs...{Colors.ENDC}")
    write_ids_to_file(output_file, num_ids, 16, 0xFFFFFFFFFFFFFFFF)

# Helper function to write IDs to file
def write_ids_to_file(output_file, num_ids, id_length, id_max):
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
    print(ASCII_TITLE)
    print(f"{Colors.HEADER}{Colors.BOLD}Flipper Zero RFID Fuzzer Generator{Colors.ENDC}")
    print(f"{Colors.OKCYAN}---------------------------------------------{Colors.ENDC}")

    while True:
        print(f"{Colors.BOLD}Select the type of ID to generate:{Colors.ENDC}")
        print(f"1. EM4100\n2. HID Prox\n3. PAC/Stanley\n4. H10301\n5. IoProx XSF\n6. Paradox\n7. Indala 26-bit\n8. Viking\n9. Pyramid\n10. Keri\n11. Jablotron\n12. Electra\n13. IDTECK\n14. Gallagher\n15. Nexwatch")
        choice = input(f"{Colors.BOLD}Enter your choice (1-15): {Colors.ENDC}").strip()

        if choice in map(str, range(1, 16)):
            num_ids = input(f"{Colors.BOLD}Enter the number of IDs to generate (default: 100,000): {Colors.ENDC}").strip()
            num_ids = int(num_ids) if num_ids.isdigit() and int(num_ids) > 0 else 100000

            output_file = input(f"{Colors.BOLD}Enter the name of the output file (default: 'dictionary.txt'): {Colors.ENDC}").strip()
            if not output_file:
                output_file = 'dictionary.txt'
            elif not output_file.endswith('.txt'):
                output_file += '.txt'

            functions = [
                generate_em4100_dictionary,
                generate_hidprox_dictionary,
                generate_pac_stanley_dictionary,
                generate_h10301_dictionary,
                generate_ioprox_xsf_dictionary,
                generate_paradox_dictionary,
                generate_indala26_dictionary,
                generate_viking_dictionary,
                generate_pyramid_dictionary,
                generate_keri_dictionary,
                generate_jablotron_dictionary,
                generate_electra_dictionary,
                generate_idteck_dictionary,
                generate_gallagher_dictionary,
                generate_nexwatch_dictionary
            ]
            script_directory = os.path.dirname(os.path.abspath(__file__))
            output_file_path = os.path.join(script_directory, output_file)
            functions[int(choice) - 1](output_file_path, num_ids)
            break
        else:
            print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")

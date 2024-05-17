import random
import sys

def generate_em4100_dictionary(output_file, num_ids):
    """
    Generates a dictionary of random EM4100 IDs and saves them to a specified file.

    Args:
        output_file (str): The name of the file to save the IDs to.
        num_ids (int): The number of IDs to generate.
    """
    try:
        with open(output_file, 'w') as file:
            for i in range(num_ids):
               
                card_id = random.randint(0, 0xFFFFFFFFFF)
                
                card_id_str = f"{card_id:010X}"

                file.write(card_id_str + '\n')

                if (i + 1) % 10000 == 0:
                    print(f"{i + 1} IDs generated...")

        print(f"EM4100 dictionary successfully generated and saved in '{output_file}'.")
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    print("Flipper Zero RFID Fuzzer: EM4100 Dictionary Generator")
    
    while True:
        try:
            num_ids_input = input("Enter the number of EM4100 identification numbers you want to generate (press Enter for 100,000): ").strip()
            if num_ids_input == '':
                num_ids = 100000
                break
            else:
                num_ids = int(num_ids_input)
                if num_ids <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    output_file = input("Enter the name of the output file (default: 'em4100_dictionary.txt'): ").strip()
    if not output_file:
        output_file = 'em4100_dictionary.txt'
    
    generate_em4100_dictionary(output_file, num_ids)


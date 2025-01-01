# F0_EM4100_generator
Flipper Zero RFID ID Generator for RFID fuzzer

# EM4100 Dictionary Generator

This Python script generates a list of random EM4100 RFID identification numbers and saves them to a text file. EM4100 is a common standard for low-frequency RFID tags, typically used in access control systems.

## Features

- Generates a specified number of random 40-bit EM4100 IDs.
- Saves the generated IDs in hexadecimal format to a text file.

## Requirements

- Python 3.x
- Fliper Zero use with RFID Fuzzer

## Usage

1. Clone the repository or download the script file `em4100_generator.py`.
2. Open a terminal or command prompt on your computer.
3. Navigate to the directory where the script is located.
4. Run the script with Python:

python em4100_generator.py

Enter the number of EM4100 identification numbers you want to generate when prompted.
Example:
Enter the number of EM4100 identification numbers you want to generate: 1000

The script will generate the specified number of IDs and save them to a text file named em4100_dictionary.txt in the same directory.

Transfer the generated em4100_dictionary.txt file to your Fliper Zero device.On Fliper Zero device, open the RFID Fuzzer application and select the option to "Load UID's from file". Choose the em4100_dictionary.txt file you transferred.Run the RFID Fuzzer to use the generated EM4100 identification numbers for testing or demonstration purposes.

## Version history
- 0.2 - Add colors, ASCII art, save in script directory, progress updates, improved input handling.
- 0.1 - Initial release raw code

## Acknowledgements
This script was created as a simple utility for generating test data for systems using EM4100 RFID tags.

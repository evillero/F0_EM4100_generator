# F0_fuzzer_generator

# RFID Fuzzer Generator

This Python script generates a list of random RFID identification numbers for various protocols, including EM4100, HID Prox, PAC Stanley, H10301, and more. It is designed for use with the Flipper Zero RFID Fuzzer.

## Features

- Generates a specified number of random RFID IDs for multiple protocols.
- Supports EM4100, HID Prox, PAC Stanley, H10301, and other common RFID standards.
- Saves the generated IDs in hexadecimal format to a text file.

## Requirements

- Python 3.x
- Flipper Zero with RFID Fuzzer
## Usage

1. Clone the repository or download the script file `fuzzer_generator.py`.
2. Open a terminal or command prompt on your computer.
3. Navigate to the directory where the script is located.
4. Run the script with Python:

python fuzzer_generator.py

Enter the number of protocol
Enter the number of identification numbers you want to generate when prompted.
Example:
Enter the number 1 for protocol EM4100 then identification numbers you want to generate 
The script will generate the specified number of IDs and save them to a text file named dictionary.txt in the same directory.

Transfer the generated dictionary.txt file to your Fliper Zero device.On Fliper Zero device, open the RFID Fuzzer application and select the option to "Load UID's from file". Choose the dictionary.txt file you transferred. Run the RFID Fuzzer to use the generated EM4100 identification numbers for testing or demonstration purposes.

## Version history
- 0.3 - 0.3 - Updated to support multiple protocols (HID Prox, PAC Stanley, H10301, etc.), improved ID generation
- 0.2 - Add colors, ASCII art, save in script directory, progress updates, improved input handling.
- 0.1 - Initial release raw code

## Acknowledgements
This script was created as a simple utility for generating test data for systems using RFID tags.

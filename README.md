# Text-to-Morse Code Converter

A simple, interactive command-line Python program that converts English text to International Morse Code.

## Features

- Interactive prompt (`$$ `)
- Real-time conversion of text to Morse code
- Proper spacing: 3 units between letters, 7 units between words
- Handles uppercase/lowercase input
- Graceful handling of unknown characters (shown as `?`)
- Runs completely offline
- Exit with `exit`, `quit` or `q`

## Requirements

- Python 3.6 or higher (works on Python 3.8+ recommended)

## Usage

1. **Open your terminal**

   - Windows: Open **Command Prompt**, **PowerShell**, or **Windows Terminal**
   - macOS: Open **Terminal**
   - Linux: Open your preferred terminal emulator

2. **Navigate to your project folder**

   ```bash
   cd path/to/your/project/folder
   (Replace with the actual path where your script is saved)

   ```

3. **Run the program**
   python main.py
   #or on some systems:
   python3 main.py
4. **How to use it**
   - A prompt $$ will appear
   - Type any English text (letters, numbers, some punctuation) and press Enter
   - The Morse code conversion appears immediately
   - Type your next message or exit
   - To quit, type one of these and press Enter:
     exit
     quit
     q

## Example sessions

$$
Hello World

Text: Hello World
Morse: .... . .-.. .-.. ---       .-- --- .-. .-.. -..

$$ 123 SOS

Text: 123 SOS
Morse: .---- ..--- ...--       ... --- ...

$$ exit
Goodbye!

## Project structure
text-to-morse/
├── main.py              # The main program file (or whatever you named it)
├── codes.py             # Contains the Morse code dictionary (morse_dict)
└── README.md            # This file you're reading now.
$$

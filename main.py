#!/usr/bin/env python3
""" """

import sys
from codes import morse_dict



# ───────────────────────────────────────────────
# Main program
# ───────────────────────────────────────────────

print("Text to Morse-code started. Type 'exit()', 'quit()', 'q()', 'q', or 'quit' to quit.\n")

try:
    while True:
        # Show prompt until user starts typing
        sys.stdout.write("$$ ")
        sys.stdout.flush()

        # Get input (the blinking stops naturally when user types)
        command = input().strip()
        converted_txt = ''

        if not command:
            continue

        if command.lower() in ('exit()', 'quit()', 'q()', 'q', 'quit', 'exit'):
            print("Goodbye!")
            break
        else:
            list_of_words = command.split()
            for idx in range(len(list_of_words)):
                word = list_of_words[idx]
                for i in range(len(word)):
                    try:
                        converted_txt += morse_dict[word[i].upper()]
                        if i < len(word) - 1:
                            converted_txt += ' ' * 3
                    except KeyError:
                        converted_text += "?"
                if idx < len(list_of_words) - 1:
                    converted_txt += ' ' * 7

        print(f"Your text: {command}\nMorse code: {converted_txt}")

except KeyboardInterrupt:
    print("\nGoodbye!")
except EOFError:
    print("\nGoodbye!")
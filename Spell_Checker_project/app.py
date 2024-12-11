#importing th erequired library
from flask import Flask, request, jsonify
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []  # List to store corrected words

        # Iterate through words in the text
        for word in words:
            corrected_word = self.spell.correction(word)
            # Check if the word is corrected
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)  # Add corrected word to the list

        # Join all corrected words back into a sentence and return
        return ' '.join(corrected_words)

    def run(self):
        print("\n---Spell Checker---")
        while True:
            text = input('Enter text to check (or type "exit" to quit): ')
            if text.lower() == 'exit':
                print('Closing the program....')
                break
            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')

if __name__ == "__main__":
    SpellCheckerApp().run()




#Translator
from googletrans import Translator
# Initialize the Translator
translator = Translator()
# Function to translate text
def translate_text(text, dest_language):
    try:
        # Translate the text to the desired language
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Taking input from the user
text_to_translate = input("Enter the text you want to translate: ")
target_language = input("Enter the target language code (e.g., 'fa' for Farsi): ")

# Translate and print the result
translated_text = translate_text(text_to_translate, target_language)

print(f"Original: {text_to_translate}")
print(f"Translated: {translated_text}")

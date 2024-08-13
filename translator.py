from googletrans import Translator

def translate_text(text, source_language, destination_language):
    translator = Translator()

    # Define language mappings if needed, otherwise googletrans supports many language codes directly.
    language_mapping = {
        'en': 'en',  # English
        'fr': 'fr',  # French
        'es': 'es',  # Spanish
        'hi': 'hi',  # Hindi
        # Add other Indian languages with proper ISO codes if supported
        # For instance:
        # 'te': 'te',  # Telugu
        # 'ta': 'ta',  # Tamil
        # 'kn': 'kn',  # Kannada
        # 'mr': 'mr',  # Marathi
    }

    # Convert the language codes
    src_lang = language_mapping.get(source_language, 'en')
    dest_lang = language_mapping.get(destination_language, 'en')

    # Perform translation
    translated = translator.translate(text, src=src_lang, dest=dest_lang)

    return translated.text

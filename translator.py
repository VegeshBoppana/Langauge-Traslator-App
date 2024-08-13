import os
from openai import AzureOpenAI

KEY = "92a0ee28127347cfbb3e2b5d828bed12"

client = AzureOpenAI(
    api_version="2023-08-01-preview",
    azure_endpoint="https://ai-proxy.lab.epam.com",
    api_key=KEY,
)

def translate_text(text, source_language, destination_language):
    # Construct a prompt for translation
    prompt = (
        f"Translate the following text from {source_language} to {destination_language}: "
        f"'{text}'"
    )

    try:
        # Use the chat model to get the translation
        response = client.chat.completions.create(
            model='gpt-4',  # You can use other models like 'gpt-35-turbo-0613'
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        translated_text = response.choices[0].message.content.strip()
        return translated_text

    except Exception as e:
        print(f"Error translating text: {e}")
        return "Translation failed."


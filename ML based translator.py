# Import necessary libraries
import torch
import nltk
nltk.download('punkt')

from transformers import MarianMTModel
from transformers import MarianTokenizer

from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Dictionary to hold model names for each translation direction
model_names = {
    "en_to_fr": "Helsinki-NLP/opus-mt-en-fr",
    "en_to_hi": "Helsinki-NLP/opus-mt-en-hi",
    "en_to_ru": "Helsinki-NLP/opus-mt-en-ru",
    "en_to_es": "Helsinki-NLP/opus-mt-en-es"
}

# Predefined reference translations for BLEU calculation
reference_translations = {
    "en_to_fr": {
        "The cat is on the mat.": "Le chat est sur le tapis.",
        "I love programming.": "J'aime la programmation.",
        # Add more pairs as needed
    },
    "en_to_hi": {
        "The cat is on the mat.": "बिल्ली चटाई पर है।",
        "I love programming.": "मुझे प्रोग्रामिंग पसंद है।",
    },
    "en_to_ru": {
        "The cat is on the mat.": "Кошка на коврике.",
        "I love programming.": "Я люблю программирование.",
    },
    "en_to_es": {
        "The cat is on the mat.": "El gato está sobre la alfombra.",
        "I love programming.": "Me encanta programar.",
    }
}

# Function to load tokenizer and model given a model name
def load_model_and_tokenizer(model_name: str):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Define the generic translation function
def translate(text: str, tokenizer, model) -> str:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)

    translated_text = tokenizer.decode(
        translated_tokens[0],
        skip_special_tokens=True
    )
    return translated_text

# Main program logic
def main():
    print("Choose translation direction:")
    print("1. English to French (en_to_fr)")
    print("2. English to Hindi (en_to_hi)")
    print("3. English to Russian (en_to_ru)")
    print("4. English to Spanish (en_to_es)")
    choice = input("Enter 1, 2, 3 or 4: ").strip()

    if choice == "1":
        direction = "en_to_fr"
        target_language = "French"
    elif choice == "2":
        direction = "en_to_hi"
        target_language = "Hindi"
    elif choice == "3":
        direction = "en_to_ru"
        target_language = "Russian"
    elif choice == "4":
        direction = "en_to_es"
        target_language = "Spanish"
    else:
        print("Invalid choice. Please restart and enter 1, 2, 3, or 4.")
        return

    print(f"Loading model for {direction} translation...")
    tokenizer, model = load_model_and_tokenizer(model_names[direction])

    input_text = input(f"Enter the English sentence to translate to {target_language}:\n")

    translated_text = translate(input_text, tokenizer, model)

    # Lookup predefined reference for BLEU
    ref_dict = reference_translations.get(direction, {})
    reference_text = ref_dict.get(input_text)

    print("\n----- Translation Result -----")
    print(f"English: {input_text}")
    print(f"{target_language}: {translated_text}")

    if reference_text:
        reference = [reference_text.strip().split()]
        candidate = translated_text.strip().split()
        smoothie = SmoothingFunction().method4
        bleu_score = sentence_bleu(reference, candidate, smoothing_function=smoothie)
        print(f"\nBLEU Score: {bleu_score:.4f}")
    else:
        print("\nNo predefined reference translation found for BLEU calculation.\n")

if __name__ == "__main__":
    main()

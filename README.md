A multilingual translation tool powered by MarianMT models from HuggingFace Transformers. This project allows you to translate English text into French, Hindi, Russian, and Spanish, and evaluates accuracy using the BLEU score. Ideal for learning NLP, machine translation, and performance benchmarking.

🚀 Features
🔄 Translate from English → French, Hindi, Russian, Spanish

🧠 Uses pre-trained models from Helsinki-NLP

📏 Calculates BLEU Score against known reference translations

💡 Simple CLI-based user interaction

🛠 Built with PyTorch, Transformers, and NLTK

🧰 Technologies Used
PyTorch

HuggingFace Transformers

MarianMT Models

NLTK

BLEU score evaluation

🛠️ Installation
bash
Copy
Edit
git clone https://github.com/your-username/ml-language-translator.git
cd ml-language-translator

pip install -r requirements.txt
You may also need to download the NLTK punkt tokenizer:

python
Copy
Edit
import nltk
nltk.download('punkt')
🧪 How to Use
Run the script:

bash
Copy
Edit
python translator.py
Choose your target language.

Enter a sentence in English.

View the translated output and BLEU evaluation (if reference exists).

📊 Example
Input:

vbnet
Copy
Edit
Sentence: The cat is on the mat.
Language: French
Output:

vbnet
Copy
Edit
English: The cat is on the mat.
French: Le chat est sur le tapis.
BLEU Score: 1.0000
📂 Reference Translations
A small set of predefined reference translations is used to calculate BLEU scores for quality evaluation. You can expand this dictionary in reference_translations.

📄 License
This project is open-source under the MIT License.
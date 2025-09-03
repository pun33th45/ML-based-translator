from flask import Flask, render_template, request
import sys
sys.path.append('.')
from ML_based_translator import translate_text

app = Flask(__name__)

def basic_translate(text, src_lang, tgt_lang):
    # Simple word replacement for demonstration
    basic_dict = {
        ('en', 'fr'): {
            'The': 'Le', 'cat': 'chat', 'is': 'est', 'on': 'sur', 'the': 'le', 'mat.': 'tapis.',
            'I': "J'", 'love': 'aime', 'programming.': 'la programmation.'
        },
        ('en', 'hi'): {
            'The': 'बिल्ली', 'cat': 'बिल्ली', 'is': 'है।', 'on': 'पर', 'the': 'चटाई', 'mat.': 'चटाई पर है।',
            'I': 'मुझे', 'love': 'पसंद है।', 'programming.': 'प्रोग्रामिंग पसंद है।'
        },
        ('en', 'ru'): {
            'The': 'Кошка', 'cat': 'Кошка', 'is': 'на', 'on': 'на', 'the': 'коврике.', 'mat.': 'коврике.',
            'I': 'Я', 'love': 'люблю', 'programming.': 'программирование.'
        },
        ('en', 'es'): {
            'The': 'El', 'cat': 'gato', 'is': 'está', 'on': 'sobre', 'the': 'la', 'mat.': 'alfombra.',
            'I': 'Me', 'love': 'encanta', 'programming.': 'programar.'
        }
    }
    key = (src_lang, tgt_lang)
    words = text.split()
    mapping = basic_dict.get(key, {})
    return ' '.join([mapping.get(w, w) for w in words])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        src_lang = request.form.get('src_lang', '')
        tgt_lang = request.form.get('tgt_lang', '')
        translation = None
        basic_translation = None
        bleu_ml = None
        bleu_basic = None
        improvement = None
        reference = None
        if text and src_lang and tgt_lang:
            translation = translate_text(text, src_lang, tgt_lang)
            basic_translation = basic_translate(text, src_lang, tgt_lang)
            from ML_based_translator import reference_translations
            direction = f"{src_lang}_to_{tgt_lang}"
            ref_dict = reference_translations.get(direction, {})
            reference = ref_dict.get(text)
            if reference:
                from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
                smoothie = SmoothingFunction().method4
                bleu_ml = sentence_bleu([reference.strip().split()], translation.strip().split(), smoothing_function=smoothie)
                bleu_basic = sentence_bleu([reference.strip().split()], basic_translation.strip().split(), smoothing_function=smoothie)
                improvement = bleu_ml - bleu_basic
        return render_template('index.html', translation=translation, basic_translation=basic_translation, bleu_ml=bleu_ml, bleu_basic=bleu_basic, improvement=improvement, reference=reference, text=text, src_lang=src_lang, tgt_lang=tgt_lang)
    else:
        # GET request: reset everything
        return render_template('index.html', translation=None, basic_translation=None, bleu_ml=None, bleu_basic=None, improvement=None, reference=None, text='', src_lang='', tgt_lang='')

if __name__ == '__main__':
    app.run(debug=True)

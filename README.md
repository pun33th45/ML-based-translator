<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>ML-Based Language Translator — README</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;max-width:740px;margin:36px auto;color:#111}
    header{display:flex;gap:16px;align-items:center}
    img.sshot{max-width:320px;border:1px solid #ddd;padding:6px;background:#fff}
    h1{font-size:20px;margin:0}
    p.small{margin:6px 0;color:#444}
    ul{margin:8px 0 12px 20px}
    pre{background:#f6f8fa;padding:10px;border-radius:6px;overflow:auto}
    .meta{font-size:13px;color:#555;margin-top:10px}
    a.button{display:inline-block;margin-top:8px;padding:8px 10px;background:#0366d6;color:#fff;text-decoration:none;border-radius:6px;font-size:13px}
    footer{margin-top:18px;font-size:12px;color:#666}
    .src-link{font-size:12px;color:#0366d6;text-decoration:none}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>ML-Based Language Translator</h1>
      <p class="small">MarianMT-based English → French / Hindi / Russian / Spanish + BLEU evaluation.</p>
    </div>

    <!-- Screenshot -->
    <img class="sshot" src="3a8ec71c-b6c7-4a1f-9aaa-6116ea5ff3a2.png" alt="ML translator screenshot">
  </header>

  <!-- Screenshot Source Link -->
  <p><a class="src-link" href="https://github.com/pun33th45/ML-based-translator/blob/bdeaaedf1bf694613b7ccd99d9c378a5f2cd7988/screenshots/output.png" target="_blank">
    🔗 Source (Screenshot)
  </a></p>

  <section>
    <ul>
      <li>Pretrained Helsinki-NLP MarianMT models</li>
      <li>BLEU score evaluation using NLTK</li>
      <li>Simple CLI interface (translator.py)</li>
    </ul>

    <strong>Quick install</strong>
    <pre>git clone https://github.com/your-username/ml-language-translator.git
cd ml-language-translator
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt')" </pre>

    <strong>Run</strong>
    <pre>python translator.py
# choose target language, enter English sentence, view ML translation + BLEU</pre>

    <!-- Research Paper -->
    <p class="meta">
      <a class="button" href="d46d3a58-2026-4a2b-a3dc-fa43d38dfa36.pdf" target="_blank">Open research paper (PDF)</a>

      <!-- Research Paper Source Link -->
      <a class="src-link" href="https://github.com/pun33th45/ML-based-translator/blob/bdeaaedf1bf694613b7ccd99d9c378a5f2cd7988/screenshots/research%20paper.pdf" target="_blank">
        🔗 Source (Research Paper)
      </a>

      <!-- Required file citation token for uploaded paper -->
      <span style="display:block;margin-top:6px">:contentReference[oaicite:0]{index=0}</span>
    </p>
  </section>

  <footer>
    <small>License: MIT — Contribute: add languages, expand reference_translations/, or improve UI.</small>
  </footer>
</body>
</html>

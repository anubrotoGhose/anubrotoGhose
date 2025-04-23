from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Load your index.html content
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('term', '').strip().lower()
    if not query:
        return "Please enter a search term."

    # Search for the query in the content
    matches = re.findall(rf'(?i)\b{re.escape(query)}\b', content)
    result_count = len(matches)

    if result_count > 0:
        return f'Found "{query}" {result_count} time(s) in the content.'
    else:
        return f'"{query}" was not found in the content.'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from translator import translate_text

app = Flask(__name__)

# Store conversation history
conversations = []

@app.route("/", methods=["GET", "POST"])
def index():
    global conversations
    if request.method == "POST":
        text = request.form['text']
        source_language = request.form['source_language']
        destination_language = request.form['destination_language']

        # Ensure text is within the character limit
        if len(text) > 348:
            return "We accept only 348 characters.", 400

        # Translate text
        translated_text = translate_text(text, source_language, destination_language)

        # Store the conversation
        conversations.append({
            "input": text,
            "output": translated_text
        })

    return render_template("index.html", conversations=conversations)

if __name__ == "__main__":
    app.run(debug=True)

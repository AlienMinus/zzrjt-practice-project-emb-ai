from flask import Flask, render_template, request
from sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text_to_analyze = request.form.get("text_to_analyze")
        if text_to_analyze.strip():
            result = sentiment_analyzer(text_to_analyze)
        else:
            result = {"error": "Input text cannot be empty. Please provide valid text to analyze."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
# main_score.py

from flask import Flask, render_template_string
from utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as score_file:
            score = score_file.read()
        # HTML template to display the score
        html = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is:</h1>
                <div id="score">{SCORE}</div>
            </body>
        </html>
        """
        return render_template_string(html)
    except Exception as e:
        print(f"Error reading score file: {e}")
        return """
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>Error:</h1>
                <div id="score style="color:red">{ERROR}</div>
            </body>
        </html>
        """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


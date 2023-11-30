from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/madlibs')
def form():
    """Show Madlibs form"""
    questions = silly_story.prompts
    print("questions:", questions)
    return render_template(
        "questions.html"
)


from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_dropdown():
    return render_template(
        "homepage.html"
    )


@app.get('/madlib-form')
def show_form():
    """Show Madlibs form"""
    # questions = silly_story.prompts
    return render_template(
        "questions.html",
        prompts=silly_story.prompts
)

@app.get('/results')
def show_story():
    """Generate answers dictionary and show Madlibs result"""
    return render_template(
        "results.html",
        story=silly_story.get_result_text(request.args)
    )


from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/madlibs')
def show_form():
    """Show Madlibs form"""
    # questions = silly_story.prompts
    return render_template(
        "questions.html",
        prompts = silly_story.prompts
)

@app.get('/results')
def show_story():
    """Generate answers dictionary and show Madlibs result"""
    answers = get_answers()
    return render_template(
        "results.html",
        story = silly_story.get_result_text(answers)
    )



def get_answers():
    """Makes and returns a dictionary made up of key/value pairs from the
    madlib form"""
    prompts = silly_story.prompts
    answers = {}
    for prompt in prompts:
        answers[prompt] = request.args.get(prompt)
    return answers
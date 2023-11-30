from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)
# TODO: Should rename the route to homepage, not madlibs, so should be "/"
@app.get('/madlibs')
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
    # TODO: Remove line 24, 32-39, redundant. Only need to pass in request.args,
    # this is already a dict like object (polymorphic to dict) made up of the
    # query items
    answers = get_answers()
    return render_template(
        "results.html",
        story=silly_story.get_result_text(answers)
    )



def get_answers():
    """Makes and returns a dictionary made up of key/value pairs from the
    madlib form"""
    prompts = silly_story.prompts
    answers = {}
    for prompt in prompts:
        answers[prompt] = request.args.get(prompt)
    return answers
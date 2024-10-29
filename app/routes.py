from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def home():
    water_facts = [
        "Water covers 71% of the Earth's surface.",
        "Only 2.5% of Earth's water is fresh water.",
        "Humans can only survive for a few days without water.",
        "Conserving water helps protect the environment."
    ]
    return render_template('home.html', facts=water_facts)

from flask import Flask, render_template_string
import random

app = Flask(__name__)

TEMPLATE = """<!DOCTYPE html>
<html><head><title>Bingo</title><style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Unica+One&display=swap');
body {{ font-family: 'Anton', sans-serif; text-align:center; background:white; padding:40px; }}
.card-container {{ display:inline-block; border:15px solid #d6452e; border-radius:20px; background:white; padding:10px 20px; }}
.header {{ background:#d6452e; color:white; padding:5px 0; border-top-left-radius:10px; border-top-right-radius:10px; }}
.name-label {{ font-family:'Unica One', sans-serif; font-size:20px; margin:0; }}
h1 {{ font-size:52px; margin:0; letter-spacing:20px; line-height:1; }}
table {{ border-collapse:collapse; margin:10px auto 0; }}
td {{ width:90px; height:60px; border:3px solid #000; background:#fff; font-size:13px; font-weight:900; padding:4px; }}
.free {{ color:#d6452e; font-size:15px; }}
</style></head><body>
<div class="card-container">
<div class="header">
<div class="name-label">JAKE RACINA'S</div>
<h1>BINGO</h1>
</div>
<table>
{% for row in grid %}
<tr>
{% for cell in row %}
<td class="{{ 'free' if cell == 'FREE' else '' }}">{{ cell }}</td>
{% endfor %}
</tr>
{% endfor %}
</table></div></body></html>
"""

WORDS = [
    "Buffalo Nickel", "Digging a Hole", "Big John’s Place", "Dead Crow", "Fill a Void",
    "Different Kind of Feeling", "Good Mood Guy", "Final Cut", "Out of Tune", "Orange Julius",
    "Same Old Dream", "I’m Going To Die", "I’m Lost", "No One Else", "Little Alien",
    "I Saw The Light", "New Hell", "Somewhere", "Another Sad Song", "Dead Man’s Drums",
    "Satellite Radio DJ", "Italian Cream", "Sometimes Sometime", "Happy Birthday JFK"
]

@app.route("/")
def bingo():
    sample = random.sample(WORDS, 24)
    grid = [sample[i*5:(i+1)*5] for i in range(5)]
    grid[2].insert(2, "FREE")
    return render_template_string(TEMPLATE, grid=grid)

if __name__ == "__main__":
    app.run(debug=True)

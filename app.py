from flask import Flask, render_template, request
from questions import questions_list
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", questions=questions_list)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    for i, question in enumerate(questions_list):
        user_answer = request.form.get(f"q{i}")
        if question.check_answer(user_answer):
            score += 1
    time_submitted = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template(
        "result.html",
        score=score,
        total=len(questions_list),
        time=time_submitted
    )

if __name__ == "__main__":
    print("App started")
    app.run(debug=True)
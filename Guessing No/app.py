from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global attempts
    feedback = ""

    if request.method == "POST":
        user_guess = int(request.form["user_guess"])
        attempts += 1

        if user_guess == secret_number:
            feedback = f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts."
        elif user_guess < secret_number:
            feedback = "Too low! Try again."
        else:
            feedback = "Too high! Try again."

    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)

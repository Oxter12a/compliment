from flask import Flask, render_template
import random

app = Flask(__name__)

insults = [
    "You have the perfect face... for radio.",
    "Your code runs as fast as my grandma—and she's 92.",
    "If laziness was an Olympic sport, you'd win gold.",
    "Your WiFi signal has more strength than your decisions.",
    "You are proof that even Google doesn't have all the answers.",
    "You're not stupid—you just have bad luck thinking.",
    "YOU are the reason i smile everytime !",
    "Your are pretty ! ... i mean pretty annoying",
    "Keep rolling your eyes, maybe you'll find a brain back there.",
    "I think i know youu , let me guess ....your are my future wife isn't? "
]

@app.route("/")
def home():
    insult = random.choice(insults)
    return render_template("index.html", insult=insult)

if __name__ == "__main__":
    app.run(debug=True)

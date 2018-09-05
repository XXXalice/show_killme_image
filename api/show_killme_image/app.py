from flask import request, Flask, redirect
from killme import Killme
import random

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome!"

@app.route("/api/killme")
def return_killme_icon():
    killme = Killme()
    icons_url = killme.fetch_images()
    result = random.choice(icons_url)
    return redirect(result)


def main():
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print("occur an error.")
        exit()


if __name__ == '__main__':
    main()
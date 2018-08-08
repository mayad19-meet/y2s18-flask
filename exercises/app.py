from flask import Flask, render_template
app = Flask(__name__)

@app.route('home.html/')
def home_page():
    players=["Lio Messi","David Beckham","Naymar"]

    return render_template("index.html",players=players,likes_same_sport=False)



if __name__ == '__main__':
   app.run(debug = True)
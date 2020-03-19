from flask import Flask, render_template
app = Flask(__name__,
static_folder="public")


@app.route("/")
def base():
   return render_template('index.html')

@app.route("/index/")
def index():
   return render_template('index.html')

@app.route("/familia/")
def familia():
   return render_template('familia.html')

@app.route("/amigos/")
def amigos():
   return render_template('amigos.html')

if __name__ == "__main__":
    app.run(debug=True)
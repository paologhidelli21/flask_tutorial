#flask_tutorial from python-3.com
#09/01/2025

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #cerca un modello specificato ("home.html") nella cartella templates. Quindi renderà il modello richiesto
    return render_template("home.html")

@app.route("/about")
#questa è la funzione che viene eseguita quando chiamo la pagina /about
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

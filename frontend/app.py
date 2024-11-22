from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/register_product")
def register_product():
    return render_template("register_product.html")

if __name__ == "__main__":
    app.run(debug=True)

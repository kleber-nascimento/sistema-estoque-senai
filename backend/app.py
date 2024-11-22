from flask import Flask, render_template
from db import db
from routes.users import users_bp
from flask_cors import CORS
from routes.products import products_bp
import os

app = Flask(__name__)
# Get absolute path to the frontend/templates directory
template_dir = os.path.abspath('../frontend/templates')
app.template_folder = template_dir
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp, url_prefix="/api")

@app.route("/register")
def index():
    return render_template("register_product.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Garante a criação das tabelas
    app.run(debug=True, port=5001)

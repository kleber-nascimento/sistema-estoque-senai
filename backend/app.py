from flask import Flask
from db import db
from routes.users import users_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Garante a criação das tabelas
    app.run(debug=True)

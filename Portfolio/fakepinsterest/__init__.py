from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "6a3bdd10c9afd98aacbc37556726653c"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = "homepage"

from fakepinsterest import routes


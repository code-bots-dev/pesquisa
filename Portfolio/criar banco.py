from fakepinsterest import database, app
from fakepinsterest.models import Usuario, Foto

with app.app_context():
    database.create_all()
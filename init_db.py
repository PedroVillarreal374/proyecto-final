from app import app, db  # Asegúrate de importar tanto la aplicación como la base de datos

with app.app_context():
    db.create_all()
    print("Base de datos inicializada.")
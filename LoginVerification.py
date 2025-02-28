# LoginVerification.py
from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required
from config.config import JWT_SECRET_KEY
from controller.auth_controller import login

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
jwt = JWTManager(app)

# Ruta de login
app.route('/login', methods=['POST'])(login)

# Ruta protegida
@app.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    return {"mensaje": "Acceso permitido a la ruta protegida"}, 200

if __name__ == '__main__':
    app.run(debug=True)

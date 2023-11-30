from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1987@localhost:5432/tasksdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

# Migración de la base de datos
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Verificar las credenciales
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout exitoso'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Procesar el formulario de registro
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        country = request.form.get('country')
        birthdate = request.form.get('birthdate')

        if not User.query.filter_by(username=username).first():
            # Crear un nuevo usuario
            new_user = User(username=username, password=password, email=email,
                            phone=phone, country=country, birthdate=birthdate)
            db.session.add(new_user)
            db.session.commit()

            # Iniciar sesión automáticamente después del registro
            login_user(new_user)

            return redirect(url_for('index'))
        else:
            return 'El nombre de usuario ya está en uso. Elige otro.'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

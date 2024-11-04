# Importation de Flask et des Blueprints depuis les modules des routes
from flask import Flask
from routes.main_routes import main_bp
#from flask_font_awesome import FontAwesome

# Création d'une application Flask
app = Flask(__name__)
#font_awesome = FontAwesome(app)
# Enregistrement le blueprint dans l'application Flask
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

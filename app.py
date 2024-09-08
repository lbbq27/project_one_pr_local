from flask import Flask
from config import config   ## del archivo congig... importa el objeto config 
from src.routes import one




app = Flask(__name__)









if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(one.main, url_prefix='/api')
    
    app.run()
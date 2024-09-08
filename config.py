from decouple import config ### libreria de Decouple para traer vaiables de entorno


class Config():
    SECRET_KEY = config('SECRET_KEY') ### creamos una variable con el mimo nombre perooo el objeto de Decouple--config me permite extraer ese valor



class DevelopmentConfig(Config):
    DEBUG =True


## esto es un diccionario - objeto

config = {
    'development': DevelopmentConfig
}

## Ahora vamos a index.py
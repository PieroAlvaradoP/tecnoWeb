from decouple import config

from app._init_ import create_app

env_config = config("ENV", cast=str, default="develop")

app = create_app(env_config)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
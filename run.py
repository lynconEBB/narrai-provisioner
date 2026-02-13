from dotenv import load_dotenv

from app import create_app
import os

load_dotenv(verbose=True, dotenv_path='.env')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv("APP_HOST"), port=os.getenv("APP_PORT"))
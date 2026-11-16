from flask import Flask
from middleware.error_middleware import register_exception_handler
from views.home_view import router as home_router
from views.about_view import router as about_router
from views.product_view import router as product_router


# create server
server = Flask(__name__)

# register controller:
server.register_blueprint(home_router)

server.register_blueprint(about_router)

server.register_blueprint(product_router)

# register middleware:
register_exception_handler(server)


# flask --app src/app.py run --debug --port 4000

# Create env folder:             py -m venv env
# Run env folder:                env/scripts/activate or for Mac: source venv/bin/activate
# Install lib:                   pip install flask
# Install lib:                   pip install python-dotenv
# Install lib:                   pip install mysql-connector-python
# Install lib:                   pip install sqlalchemy
# Create requirements.txt file:  pip freeze > requirements.txt
# Restore libraries:             pip install -r requirements.txt
# Upgrade pip:                   python.exe -m pip install --upgrade pip
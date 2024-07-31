from routes import app
from flask import Flask
# above are the old imports...
# Import the routes after initializing the Flask app


# from flask import Flask
# app = Flask(__name__)
# # Import routes after creating the app instance
# from routes import *

# if __name__ == '__main__':
#      app.run(host="0.0.0.0", port=8000)


# app = Flask(__name__)

if __name__ == '__main__':
    from routes import *
    app.run(host="0.0.0.0", port=8000)
else:
    from routes import *
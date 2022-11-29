from app import app
from flask_cors import CORS
from api.method_api import method_route

app.register_blueprint(method_route, url_prefix='/method')

CORS(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
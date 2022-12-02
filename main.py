from app import app
from flask_cors import CORS
from controls.api.method_api import method_route
from controls.api.config_api import config_route
from controls.api.data_file_api import data_file_route
from controls.api.error_file_api import error_file_route

app.register_blueprint(method_route, url_prefix='/method')
app.register_blueprint(config_route, url_prefix='/config')
app.register_blueprint(data_file_route, url_prefix='/data_file')
app.register_blueprint(error_file_route, url_prefix='/error_file')

CORS(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

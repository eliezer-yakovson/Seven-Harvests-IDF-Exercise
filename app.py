from flask import Flask
from routes.assign_routes import assign_bp
from routes.report_routes import report_bp
from routes.db_init_route import db_bp

app = Flask(__name__)

app.register_blueprint(assign_bp)
app.register_blueprint(report_bp)
app.register_blueprint(db_bp)

if __name__ == "__main__":
    app.run(debug=True)

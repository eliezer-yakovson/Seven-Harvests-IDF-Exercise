from flask import Blueprint, jsonify
from db.initialize_schema import initialize_schema


db_bp = Blueprint("db", __name__)


@db_bp.post("/initDb")
def init_db():
    initialize_schema()
    return jsonify({"message": "DB initialized successfully"})

from flask import Blueprint, jsonify, request
from repository.sql_repo import SQLRepo


report_bp = Blueprint("report", __name__)
repo = SQLRepo()


@report_bp.get("/space")
def space():
    return jsonify(repo.get_space_report())


@report_bp.get("/waitingList")
def waiting():
    return jsonify(repo.get_waiting_list())




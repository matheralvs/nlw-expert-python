from flask import Blueprint, request, jsonify
from src.errors.error_handle import handle_errors
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    response = None
    try:
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as expection:
        response = handle_errors(expection)

    return jsonify(response.body), response.staus_code

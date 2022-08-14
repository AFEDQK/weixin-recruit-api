from flask import Blueprint

from app.api import views as v

bp = Blueprint("msgProcess/v1", __name__)

# session view

bp.add_url_rule(
    "/findJob",
    view_func=v.FindJob.as_view(name="findJob"),
    methods=["GET"],
)
bp.add_url_rule(
    "/recruit",
    view_func=v.GetParseResult.as_view(name="recruit"),
    methods=["GET"],
)

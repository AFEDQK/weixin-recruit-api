import logging

from flask import jsonify, request
from flask.views import MethodView
from app.utils.get_parse_data import seg_punc, find_job


class FindJob(MethodView):

    @staticmethod
    def get():
        original_text = request.form.get("text", None)
        if not original_text:
            logging.info("The input text is empty")
        job_info = find_job(original_text)
        return jsonify(job_info)


class GetParseResult(MethodView):

    @staticmethod
    def get():
        original_text = request.form.get("text", None)
        if not original_text:
            logging.info("The input text is empty")
        parse_result = seg_punc(original_text)
        return jsonify(parse_result)

import logging

from flask import Flask, request, jsonify
from app.exceptions import InputNotFound

from app.utils.get_parse_data import find_job, seg_punc

app = Flask(__name__)
app.secret_key = "sdfsdfasdf"


@app.route("/msgProcess/findJob", methods=["POST"])
def findJob():
    original_text = request.form.get("text", None)
    if original_text is None:
        original_text = request.args.get("text", None)
    if not original_text:
        raise InputNotFound(original_text)
    job_info = find_job(original_text)
    return jsonify(job_info)


@app.route("/msgProcess/recruit", methods=["POST"])
def recruit():
    original_text = request.form.get("text", None)
    if original_text is None:
        original_text = request.args.get("text", None)
    if not original_text:
        raise InputNotFound(original_text)
    parse_result = seg_punc(original_text)
    return jsonify(parse_result)


app.run(port=2022, host="0.0.0.0", debug=True)

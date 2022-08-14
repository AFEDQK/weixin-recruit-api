import logging

from flask import Flask, request, jsonify

from app.utils.get_parse_data import find_job, seg_punc

app = Flask(__name__)
app.secret_key = "sdfsdfasdf"


@app.route("/msgProcess/findJob", methods=["GET"])
def findJob():
    original_text = request.form.get("text", None)
    if not original_text:
        logging.info("The input text is empty")
    job_info = find_job(original_text)
    return jsonify(job_info)


@app.route("/msgProcess/recruit", methods=["GET"])
def recruit():
    original_text = request.form.get("text", None)
    if not original_text:
        logging.info("The input text is empty")
    parse_result = seg_punc(original_text)
    return jsonify(parse_result)


app.run(port=2022, host="0.0.0.0", debug=True)

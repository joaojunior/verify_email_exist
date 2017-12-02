from flask import Flask, jsonify, request

from validate_email import validate_email

app = Flask(__name__)


@app.route("/check", methods=['POST'])
def check_email():
    content = request.get_json()
    if content is not None:
        email = content.get('email', '')
        if validate_email(email) is False:
            result = {'exist': False,
                      'message': "This e-mail is invalid"}
    return jsonify(result)

from flask import Flask, jsonify, request

from validate_email import validate_email

app = Flask(__name__)


EMAIL_DONT_EXIST = "This e-mail doesn't exist"
EMAIL_EXIST = 'This e-mail exist'
EMAIL_INVALID = 'This e-mail is invalid'


@app.route("/check", methods=['POST'])
def check_email():
    content = request.get_json()
    if content is not None:
        email = content.get('email', '')
        if validate_email(email) is False:
            result = {'exist': False,
                      'message': EMAIL_INVALID}
        elif validate_email(email, verify=True) is False:
            result = {'exist': False,
                      'message': EMAIL_DONT_EXIST}
        else:
            result = {'exist': True,
                      'message': EMAIL_EXIST}
    return jsonify(result)

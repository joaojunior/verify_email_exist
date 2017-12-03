from flask import Flask, jsonify, request, render_template

from validate_email import validate_email

app = Flask(__name__,
            static_url_path='',
            static_folder='static')


EMAIL_DONT_EXIST = "This e-mail doesn't exist"
EMAIL_EXIST = 'This e-mail exist'
EMAIL_INVALID = 'This e-mail is invalid'


@app.route('/', methods=['GET'])
def metrics():
    return render_template('index.html')


@app.route("/check", methods=['POST'])
def check_email():
    content = request.get_json()
    if content is not None:
        email = content.get('email', '')
        if validate_email(email) is False:
            result = {'exist': False,
                      'message': EMAIL_INVALID}
        elif validate_email(email, verify=True) is True:
            result = {'exist': True,
                      'message': EMAIL_EXIST}
        else:
            result = {'exist': False,
                      'message': EMAIL_DONT_EXIST}
    return jsonify(result)


if __name__ == "__main__":
    app.run()

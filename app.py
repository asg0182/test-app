from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'SERVER_SOFTWARE': request.environ.get('SERVER_SOFTWARE'),
        'REQUEST_METHOD': request.environ.get('REQUEST_METHOD'),
        'SCRIPT_NAME': request.environ.get('SCRIPT_NAME'),
        'PATH_INFO': request.environ.get('PATH_INFO'),
        'QUERY_STRING': request.environ.get('QUERY_STRING'),
        'REMOTE_ADDR': request.environ.get('REMOTE_ADDR'),
        'REMOTE_PORT': request.environ.get('REMOTE_PORT'),
        'SERVER_NAME': request.environ.get('SERVER_NAME'),
        'HTTP_HOST': request.environ.get('HTTP_HOST'),
        'HTTP_USER_AGENT': request.environ.get('HTTP_USER_AGENT'),
    })


if __name__ == '__main__':
    app.run()

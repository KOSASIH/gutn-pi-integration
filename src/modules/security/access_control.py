import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/api/data', methods=['GET'])
def access_control():
    """
    Control access to the data API.

    Returns:
    flask.Response: Response object
    """
    if request.headers.get('Authorization') == 'Bearer <access_token>':
        data = collect_data(['<data_source>'])
        insights = analyze_data(data)
        return flask.jsonify(insights)
    else:
        return flask.Response('Unauthorized', 401)

if __name__ == '__main__':
    app.run()

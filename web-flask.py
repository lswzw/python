import flask

server = flask.Flask(__name__)

@server.route("/")

def web():
    return "<h1>This Is Python!</h1>"

if __name__ == "__main__":
    server.run(host='0.0.0.0',port=80)


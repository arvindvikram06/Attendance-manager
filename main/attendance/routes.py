from .. import app

@app.route("/attendance", methods=["POST", "GET"])
def attendance():
    return "hello"
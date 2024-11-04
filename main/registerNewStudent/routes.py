from flask import Response
from .. import app
from . import video_capturing_for_registration


@app.route("/video_rendering_for_reg", methods=["POST", "GET"])
def video_rendering_for_reg():
    return Response(video_capturing_for_registration(1), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/registration", methods=["POST", "GET"])
def registration():
    return "Welcome to Registration page"

# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
)
import os

from online_fiducial_boards.utils import flash_errors
from online_fiducial_boards.extensions import csrf_protect

from fiducial_boards_generator.fiducial_library import ARUCO_DICT
from fiducial_boards_generator.boards_generator import BoardsGenerator

blueprint = Blueprint("public", __name__, static_folder="../static")

SCRIPT_PATH = os.path.dirname(__file__)

generator = BoardsGenerator(os.path.join(SCRIPT_PATH, "../static"),
                            "../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")


    return render_template("public/home.html")

@blueprint.route("/about/")
def about():
    """About page."""
    return render_template("public/about.html")


@blueprint.route("/contact/")
def contact():
    """Contact page."""
    return render_template("public/contact.html")

@blueprint.route("/original/")
def original():
    """Original board generation page."""
    if request.method == "GET":
       print("get")
    elif request.method == "POST":
       print("post")

    fiducialLibs = ARUCO_DICT.keys()
    return render_template("public/original.html", fiducialLibs=fiducialLibs)



@blueprint.route('/original/update_data', methods=["POST"])
@csrf_protect.exempt
def update_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        image_url = generator.generate_original(data)
    except Exception as e:
        return jsonify({'error': e}), 400

    return jsonify({'image_url': image_url}), 200



@blueprint.route("/manual/")
def manual():
    """Contact page."""
    return render_template("public/manual.html")


@blueprint.route("/carpet/")
def carpet():
    """Serpinski carpet based fiducial generation  page."""
    return render_template("public/carpet.html")
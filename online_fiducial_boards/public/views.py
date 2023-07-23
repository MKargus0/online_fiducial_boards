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


from online_fiducial_boards.utils import flash_errors
from online_fiducial_boards.extensions import csrf_protect

from fiducial_boards_generator.fiducial_library import ARUCO_DICT
from fiducial_boards_generator.boards_generator import BoardsGenerator

blueprint = Blueprint("public", __name__, static_folder="../static")
generator = BoardsGenerator(static_folder="../static")


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

    # select_value = data.get('select_value')
    # input1_value = data.get('input1_value')
    # input2_value = data.get('input2_value')
    
    # if not all([select_value, input1_value, input2_value]):
    #     return jsonify({'error': 'Missing values'}), 400
    
    # generator.generate_original()
    # # Generate the picture and get its URL
    # image_url = "assets/img/aruco_orig.png" #generate_picture(select_value, input1_value, input2_value)

    # return jsonify({'image_url': image_url})



@blueprint.route("/manual/")
def manual():
    """Contact page."""
    return render_template("public/manual.html")


@blueprint.route("/carpet/")
def carpet():
    """Serpinski carpet based fiducial generation  page."""
    return render_template("public/carpet.html")
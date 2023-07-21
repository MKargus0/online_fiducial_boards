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
)


from online_fiducial_boards.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")



@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
       pass

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
    """Contact page."""
    fiducialLibs = ['Apple', 'Banana', 'Orange', 'Mango', 'Strawberry']
    return render_template("public/original.html", fiducialLibs=fiducialLibs)


@blueprint.route("/manual/")
def manual():
    """Contact page."""
    return render_template("public/manual.html")


@blueprint.route("/carpet/")
def carpet():
    """Contact page."""
    return render_template("public/carpet.html")
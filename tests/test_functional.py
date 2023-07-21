# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
from flask import url_for

from online_fiducial_boards.user.models import User

from .factories import UserFactory


# class TestLoggingIn:
#     """Login."""

#     def test_can_log_in_returns_200(self, user, testapp):
#         """Login successful."""
#         # Goes to homepage
#         res = testapp.get("/")
#         # Fills out login form in navbar
#         form = res.forms["loginForm"]
#         form["username"] = user.username
#         form["password"] = "myprecious"
#         # Submits
#         res = form.submit().follow()
#         assert res.status_code == 200

#     def test_sees_alert_on_log_out(self, user, testapp):
#         """Show alert on logout."""
#         res = testapp.get("/")
#         # Fills out login form in navbar
#         form = res.forms["loginForm"]
#         form["username"] = user.username
#         form["password"] = "myprecious"
#         # Submits
#         res = form.submit().follow()
#         res = testapp.get(url_for("public.logout")).follow()
#         # sees alert
#         assert "You are logged out." in res

#     def test_sees_error_message_if_password_is_incorrect(self, user, testapp):
#         """Show error if password is incorrect."""
#         # Goes to homepage
#         res = testapp.get("/")
#         # Fills out login form, password incorrect
#         form = res.forms["loginForm"]
#         form["username"] = user.username
#         form["password"] = "wrong"
#         # Submits
#         res = form.submit()
#         # sees error
#         assert "Invalid password" in res

#     def test_sees_error_message_if_username_doesnt_exist(self, user, testapp):
#         """Show error if username doesn't exist."""
#         # Goes to homepage
#         res = testapp.get("/")
#         # Fills out login form, password incorrect
#         form = res.forms["loginForm"]
#         form["username"] = "unknown"
#         form["password"] = "myprecious"
#         # Submits
#         res = form.submit()
#         # sees error
#         assert "Unknown user" in res
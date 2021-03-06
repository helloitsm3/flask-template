from flask import Blueprint, render_template, request, redirect, url_for


api_data = Blueprint("main_api", __name__)


@data.route("/home")
def getHome():
    return '{"Data": "Welcome to the homepage"}'


@data.route("/")
def main():
    return render_template("main.html")

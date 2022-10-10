from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


category_blueprint= Blueprint("category", __name__)

@category_blueprint.route("/category/add")
def add_category():
    return render_template("category/add.html")

@category_blueprint.route("/category")
def category():
    return render_template("category/index.html")
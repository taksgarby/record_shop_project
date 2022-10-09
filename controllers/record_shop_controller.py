from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository

record_shop_blueprint= Blueprint("record_shop", __name__)

@record_shop_blueprint.route("/records")
def records():
    records = record_repository.select_all()
    return render_template("records/index.html", all_records = records)

@record_shop_blueprint.route("/add")
def add():
    return render_template("add.html")


@record_shop_blueprint.route("/records/<id>", methods=['GET'])
def show_record(id):
    return render_template('records/show.html', record = record_repository.select(id))


@record_shop_blueprint.route("/artists")
def artists():
    return render_template("artists/index.html")
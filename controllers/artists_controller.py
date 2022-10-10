
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


artists_blueprint= Blueprint("artists", __name__)

@artists_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", all_artists = artists)


@artists_blueprint.route("/artists/add", methods= ['GET'])
def add_artist():
    
    return render_template("artists/add.html")

@artists_blueprint.route("/artists/<id>", methods=['GET'])
def show_artist(id):
    return render_template('artists/show.html', 
    artist = artist_repository.select(id), all_records = record_repository.select_all())

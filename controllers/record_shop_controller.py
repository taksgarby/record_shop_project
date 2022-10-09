
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

@record_shop_blueprint.route("/add", methods= ['GET'])
def add():
    return render_template("add.html", all_artists = artist_repository.select_all())


@record_shop_blueprint.route("/records", methods=['POST'])
def create_record():
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    stock_count = request.form['stock_count']
    buying_cost = request.form['buying_cost']
    price = request.form['price']
    artist_id = request.form['artist_id']
    artist = artist_repository.select(artist_id)
    record = Record(title, artist, genre, year, stock_count, buying_cost, price)
    record_repository.save(record)
    return redirect('/records')


@record_shop_blueprint.route("/records/<id>", methods=['GET'])
def show_record(id):
    return render_template('records/show.html', record = record_repository.select(id))


@record_shop_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", all_artists = artists)


@record_shop_blueprint.route("/artists/add", methods= ['GET'])
def add_artist():
    
    return render_template("artists/add.html")

@record_shop_blueprint.route("/artists/<id>", methods=['GET'])
def show_artist(id):
    return render_template('artists/show.html', artist = artist_repository.select(id))
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scraper



app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)


@app.route('/')
def home():
    mars_info = mongo.db.mars_mongo.find_one()
    return render_template('home.html' , mars_info = mars_info)


@app.route('/scrape')
def scrape():
    mars_mongo = mongo.db.mars_mongo
    mars_info = scrape_mars.scraper()
    mars_mongo.update({}, mars_info, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)
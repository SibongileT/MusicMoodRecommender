from flask import Flask, request, render_template
import flask
import os
from reccomender_functions import get_songs,get_recommendations


app = Flask(__name__)

## Put your work here. You are also free to use static/css and templates/ if you would like
@app.route('/')
def hello_world():
    songs,artists,ids = get_songs()
    return flask.render_template('base.html',songs=songs,artists=artists,ids=ids)


@app.route('/playlist')
def playlist_recommendation():
    #print(flask.request.args)
    song = flask.request.args.get("Song")
    energy = flask.request.args.get("Energy")
    valence = flask.request.args.get("Valence")
    print(energy)
    print(valence)
    #try:
    song_ids = get_recommendations(song,float(valence),float(energy))
    
    return flask.render_template('playlist.html',song_ids=song_ids)
    # except:
    #     return flask.render_template("error.html")

@app.route('/about')
def about():
    return render_template('about.html', title='about')



## This just gets flask running
if __name__ == "__main__":
    app.run(debug=True)

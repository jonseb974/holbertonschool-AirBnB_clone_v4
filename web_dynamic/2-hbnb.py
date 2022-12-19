#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
import uuid
from flask import Flask, render_template, url_for
from models import storage
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/2-hbnb/') # '/2-hbnb'
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states, cities & amenities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('2-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

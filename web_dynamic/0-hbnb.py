#!/usr/bin/python3
"""
Flask app integrates in AirBnB HTML template.
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

# Set up for flask
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'



# flask rendering
@app.teardown_appcontext
def teardown_db(exception):
	"""
	after each request, the method calls .close(), .remove() on
	current SQLAlchemy Session
	"""
	storage.close()


@app.route('/0-hbnb/')
def hbnh_filters(the_id=None):
	"""
	Custom template with states, cities, amenities.
	"""
	state_objs = storage.all('State').values()
	states = dict([state.name, state] for state in state_objs)
	amens = storage.all('Amenity').values()
	places = storage.all('Places').vales()
	users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
		          for user in storage.all('User').value())
	cache_id = (str(uuid.uuid4()))
	return render_template('1-hbnb.html',
		                    states=states,
		                    amens=amens,
		                    places=places,
		                    users=users,
		                    cache_id=cache_id)


if __name__ == '__main__':
	"""
	The main Flask app
	"""
	app.run(host=host, port=port)
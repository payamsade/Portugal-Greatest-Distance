import geojson
import geopy

class GeoCalculator():

	def load_geo_data(self, filepath):
		with open(filepath) as f:
			geo_data = geojson.load(f)
		coordinates = geo_data["coordinates"]
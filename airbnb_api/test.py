# """Flask App for Predicting Optimal AirBnB prices in Berlin"""
# from flask import Flask, jsonify, request
# import numpy as np
# import pandas as pd
# import pickle
# from joblib import load
# import xgboost as xgb
#
# # local import:
# # from .api_function import get_lemmas
# from dotenv import load_dotenv
# load_dotenv()
#
# # create app:
#
# app = Flask(__name__)
#
#     # load pipeline pickle:
# pipeline1 = load('airbnb_api/test2_regression.pkl')
#
# @app.route('/', methods=['GET', 'POST'])
# def root():
#     """Root site directory for the app.Renders only the base.html template.
#        :return: render_template
#     """
#     # message = 'welcome home'
#     return ""
#
#
# @app.route('/request', methods=['GET', 'POST'])
# def request_data():
#     """Gets data in JSON format and runs it through the model.
#        :return: JSON file.
#     """
#     data = request.get_json()
#
#     # Non-default values. Needs to have user input or breaks the app.
#     # TODO Accomodate has a spelling error. Needs to be changed to "accommodate".
#     accommodates = listings["accommodates"]
#     bathrooms = listings["bathrooms"]
#     bedrooms = listings["bedrooms"]
#     size = ["size"]
#     room_type = listings["room_type"]
#     bed_type = listings["bed_type"]
#     minimum_nights = listings["minimum_nights"]
#     instant_bookable = listings["instant_bookable"]
#     cancellation_policy = listings["cancellation_policy"]
#     bag_of_words = listings["bag_of_words"]
#
#
#
#     features = {'accommodates': accommodates,
#     'bathrooms': bathrooms,
#     'bedrooms': bedrooms,
#     'size': size,
#     'room_type': room_type,
#     'bed_type': bed_type,
#     'minimum_nights': minimum_nights,
#     'instant_bookable': instant_bookable,
#     'cancellation_policy': cancellation_policy,
#     'bag_of_words': bag_of_words}
#
#     # Converts the data into a DataFrame object.
#     predict_data = pd.DataFrame(features, index=[1])
#
#
#     # Feeds the data into the model.
#     prediction = pipeline1.predict(predict_data)
#
#     # Returns prediction in a JSON format and within, a float.
#     return jsonify({'prediction': prediction[0]})
#
#
# if __name__ == '__main__':
#     APP.run(debug=True)

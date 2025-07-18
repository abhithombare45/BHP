import json
import pickle
import os

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("Loading the saved Artifacts... Starts ->")
    global __data_columns
    global __locations
    global __model

    base_dir = os.path.dirname(__file__)

    # Relative path for columns.json
    columns_path = os.path.join(base_dir, "artifacts", "columns.json")
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    # Relative path for model pickle
    model_path = os.path.join(base_dir, "artifacts", "banglore_home_prices_model.pickle")
    with open(model_path, "rb") as f:
        __model = pickle.load(f)

    print("Loading Artifacts is Done!\n")

def get_location_names():
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = [0] * len(__data_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

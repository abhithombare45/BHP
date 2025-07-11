import json
import pickle

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("Loading the saved Artifacts... Starts ->")
    global __data_columns
    global __locations
    global __model

    with open("/Users/abhijeetthombare/ab_lib/Projects/BangloreHousePrices/server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("/Users/abhijeetthombare/ab_lib/Projects/BangloreHousePrices/server/artifacts/banglore_home_prices_model.pickle", "rb") as f:
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

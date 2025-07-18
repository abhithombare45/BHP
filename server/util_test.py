import json
import pickle
import numpy as np
import os

# import sklearn as sl
# scikit-learn

__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    # return round(float(__model.predict([x])[0]), 2)    # Originally it was like this
    return round(__model.predict([x])[0], 2)

    # return __model.predict([x])


def load_saved_artifacts():
    print("Loading the saved Artifacts... Starts ->")
    global __data_columns
    global __locations

#    with open("/Users/abhijeetthombare/ab_lib/Projects/BangloreHousePrices/server/artifacts/columns.json","r",) as f:
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "artifacts", "columns.json"), "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    global __model
    with open(
        "/Users/abhijeetthombare/ab_lib/Projects/BangloreHousePrices/server/artifacts/banglore_home_prices_model.pickle",
        "rb",
    ) as f:
        __model = pickle.load(f)
    print("Loading Artifacts is Done!")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())

    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 2))
    print(get_estimated_price("Kalhalli", 1000, 2, 2))  # other location
    print(get_estimated_price("Ejipura", 1000, 2, 2))  # other location

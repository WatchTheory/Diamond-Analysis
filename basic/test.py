import pickle

try:
    with open('EDA_alumni.pkl', 'rb') as f:
        loaded_data = pickle.load(f)
    
    print("Type of loaded data:", type(loaded_data))
    
    if isinstance(loaded_data, dict):
        print("Dictionary keys:", list(loaded_data.keys()))
        # Optionally, check types of values
        for key, value in loaded_data.items():
            print(f"Key '{key}' has type: {type(value)}")
    else:
        print("Not a dictionary. Available attributes/methods:", dir(loaded_data))
except Exception as e:
    print(f"Error loading pickle: {e}")
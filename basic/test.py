<<<<<<< HEAD
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
=======
version https://git-lfs.github.com/spec/v1
oid sha256:7648685bb8394615fb8d50651d9264d3f03a05fd192e72c242da50f4219518bc
size 566
>>>>>>> 96f5544 (added baisc file)

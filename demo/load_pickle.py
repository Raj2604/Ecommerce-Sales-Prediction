import pickle

# Specify the path to your .pkl file
file_path = './xgboost_model_reg.pkl'  # Change this to your file path

try:
    # Open the .pkl file in binary read mode
    with open(file_path, 'rb') as file:
        # Load the object from the file
        loaded_object = pickle.load(file)

    # Print or use the loaded object as needed
    print(loaded_object)

except Exception as e:
    print(f"Error loading the pickle file: {e}")

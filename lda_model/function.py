import pickle

file_name ="lda.sav"
def load_lda_model(file_name=file_name):
    with open(file_name, 'rb') as file:
        model = pickle.load(file)
    return model

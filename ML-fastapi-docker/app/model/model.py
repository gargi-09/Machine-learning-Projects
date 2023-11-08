import pickle
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/logistic_model.pkl","rb") as f:
    model = pickle.load(f)


def predict_pipe(doc):
    pred = model.predict([doc])
    return pred[0]
# print(predict_pipe([0,0,1,0,5849,0.0,127.0,360.0,1,1,0,1]))
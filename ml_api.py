from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    Size: float
    Weight: float
    Sweetness: float
    Crunchiness: float
    Juiciness: float
    Ripeness: float
    Acidity: float

# Loading the saved model
apple_model = pickle.load(open('apple_quality_model.pkl', 'rb'))

@app.post('/quality_prediction')
def quality_pred(input_parameters: model_input):
    input_list = [
        input_parameters.Size,
        input_parameters.Weight,
        input_parameters.Sweetness,
        input_parameters.Crunchiness,
        input_parameters.Juiciness,
        input_parameters.Ripeness,
        input_parameters.Acidity
    ]

    prediction = apple_model.predict([input_list])

    if prediction[0] == 0:
        return "The quality of apple is bad"
    else:
        return "The quality of apple is good"

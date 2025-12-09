import sqlite3

from utils.config import settings
from data import SQLRepository
from fastapi import FastAPI
from models.model import GarchModel
from pydantic import BaseModel
import os 

db_path = os.path.basename(settings.db_name)
models_path = os.path.basename(settings.model_directory)

#`FitIn` class
class FitIn(BaseModel):
    ticker: str
    use_new_data: bool
    n_observations: int
    p: int
    q: int

#`FitOut` class
class FitOut(FitIn):
    success: bool
    message: str
    
#`PredictIn` class
class PredictIn(BaseModel):
    ticker : str
    n_days : int


#`PredictOut` class
class PredictOut(PredictIn):
    success: bool 
    forecast: dict
    message: str


def build_model(ticker  ,use_new_data):
    # Create DB connection
    connection = sqlite3.connect(db_path, check_same_thread=False)

    # Create `SQLRepository`
    repo = SQLRepository(connection=connection)

    # Create model
    model = GarchModel(ticker=ticker ,repo=repo, use_new_data=use_new_data, model_directory=models_path)

    # Return model
    return  model


app = FastAPI()


#"/fit" path, 200 status code
@app.post("/fit" ,status_code=200 , response_model=FitOut)
def fit_model(request: FitIn):
    """Fit model, return confirmation message.

    Parameters
    ----------
    request : FitIn

    Returns
    ------
    dict
        Must conform to `FitOut` class
    """
    # Create `response` dictionary from `request`
    response =request.dict()

    # Create try block to handle exceptions
    try:
        # Build model with `build_model` function
        model=build_model(ticker=request.ticker ,use_new_data=request.use_new_data)

        # Wrangle data
        model.wrangle_data(n_observations=request.n_observations)

        # Fit model
        model.fit(p=request.p,q=request.q)

        # Save model
        file_name = model.dump()

        # Add `"success"` key to `response`
        response["success"]=True

        # Add `"message"` key to `response` with `filename`
        response["message"]= f"Trained and saved '{file_name}'."

    # Create except block
    except Exception as e :
        # Add `"success"` key to `response`

        response["success"]=False

        # Add `"message"` key to `response` with error message
        response["message"]=str(e)
        
        
    # Return response

    return response


# "/predict" path, 200 status code
@app.post("/predict" ,status_code=200 ,response_model =PredictOut)
def get_prediction(request :PredictIn):
    # Create `response` dictionary from `request`
    response =request.dict()

    # Create try block to handle exceptions
    try :
        # Build model with `build_model` function
        model = build_model(ticker=request.ticker ,use_new_data=False)

        # Load stored model
        model.load()

        # Generate prediction
        prediction =model.predict_volatility(horizon=request.n_days)

        # Add `"success"` key to `response`
        response["success"]=True

        # Add `"forecast"` key to `response`
        response["forecast"]=prediction

        # Add `"message"` key to `response`
        response["message"]=""

    # Create except block
    except Exception as e:
        # Add `"success"` key to `response`
        response["success"] = False

        # Add `"forecast"` key to `response`
        response["forecast"] = {}

        #  Add `"message"` key to `response`
        response["message"]=str(e)

    # Return response
    return response

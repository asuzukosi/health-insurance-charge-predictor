import pickle


def model_predictor(model_input: list) -> float:
    """
    This function is used to predict the insurance charge
    
    Args:
        model_input: list of input values
        
    Returns:
        float: predicted insurance charge
    """
    with open("services/trained_model/regression.pkl", 'rb') as predictor_model:
        # Load the model
        model = pickle.load(predictor_model)
        charge = model.predict([model_input])
        return charge
from torch import nn

# Fonction to validate the amount and the model
def validate_amount(amount, model):
    if amount < 0 or amount > 1:
        raise ValueError("The amount should be between 0 and 1")
    if not isinstance(model, nn.Module):
        raise ValueError("The model should be an instance of torch.nn.Module")
    if not isinstance(amount, (int, float)):
        raise ValueError("The amount should be an integer or a float") 
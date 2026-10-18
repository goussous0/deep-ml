import math
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
    total = sum([ math.exp(_) for _ in scores])
    
    return [math.log((math.exp(item)/total)) for item in scores]
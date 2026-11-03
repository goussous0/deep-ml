import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = np.arange(n_samples)
    if shuffle is True:
        np.random.shuffle(indices)
        

    r = indices.shape[0] % k
    s = indices.shape[0] // k
    # print (r,s )

    tmp = []
    for i in range(0, indices.shape[0], s):
        test = indices[i:i+s].tolist()
        train = indices[:i].tolist() + indices[i+s:].tolist() 
        tmp.append((train, test))


    return tmp

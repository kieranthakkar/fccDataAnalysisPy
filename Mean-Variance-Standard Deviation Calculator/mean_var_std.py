import numpy as np

def calculate(list) -> dict:
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    a = np.array([list[0:3],list[3:6],list[6:]]) 
    
    mean = [a.mean(axis=0).tolist(),a.mean(axis=1).tolist(),a.mean()]
    var = [a.var(axis=0).tolist(),a.var(axis=1).tolist(),a.var()]
    std = [a.std(axis=0).tolist(),a.std(axis=1).tolist(),a.std()]
    max = [a.max(axis=0).tolist(),a.max(axis=1).tolist(),a.max()]
    min = [a.min(axis=0).tolist(),a.min(axis=1).tolist(),a.min()]
    sum = [a.sum(axis=0).tolist(),a.sum(axis=1).tolist(),a.sum()]
    
    calculations = {'mean': mean, 'variance': var, 'standard deviation': std, 'max': max, 'min': min, 'sum': sum}
    return calculations
from sklearn.metrics import accuracy_score as accuracy , precision_score as precision , recall_score as recall , f1_score as f1 
import numpy as np
import time

def metrics_info(y_true,y_pred):
    metrics = {
        "accuracy":accuracy(y_true,y_pred),
        "precision":precision(y_true,y_pred),
        "recall":recall(y_true,y_pred),
        "f1_score":f1(y_true,y_pred)
    }
    return metrics

def calculate_training_time(start_time, end_time):
    training_time_seconds = end_time - start_time
    training_time_minutes = training_time_seconds / 60

    return {
        "seconds":training_time_seconds,
        "minutes": training_time_minutes
    }
#how long it takes to make a prediction
def calculate_inference_time(model,test_data):
    times = []
    for testData in test_data:
        start = time.time()
        model.predict([testData])
        times.append(time.time()-start)
    
    return np.mean(times)
import functools
import time
import logging
from typing import Callable,Any

logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")
logger=logging.getLogger(__name__)



def ai_telemetry(func: Callable[...,Any]) -> Callable[Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs: Any)-> Any:
        start_time=time.perf_counter()
        logger.info(f"Starting execution of {func.__name__} with args: {args}, kwargs:{kwargs}")
        try:
            result=func(*args,**kwargs)
            elapsed_time=time.perf_counter()-start_time
            logger.info(f"successfully executed in {elapsed_time:.4f}seconds")
            return result
        except Exception as e:
            elapsed_time=time.perf_counter()-start_time
            logger.error(f"Error occured during execution of {func.__name__}:{e}")
            raise
    return wrapper
    
@ai_telemetry
def simulate_ai_model_training(epochs:int,batch_size:int)-> str:
    time.sleep(1.5)
    if epochs<=0:
        raise ValueError("Number of epochs must be greater than zero")
    return f"Model trained successfully for {epochs} epochs with batch size{batch_size}"

if __name__=="__main__": 
    print("Running test 1: succesful execution")
    try:
             output=simulate_ai_model_training(epochs=5,batch_size=32)
             print(output)
    except Exception:
         pass
    print("\n Running Test 2 : error handling")
    try:
         simulate_ai_model_training(epochs=0,batch_size=32)
    except ValueError :
         print("Caught expected ValueError successfully")

    

    
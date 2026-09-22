Ai tememetry Decorator
a lightweight and advanced python utility decorator designed to track execution time,handle exceptions and log telemetry data for AI and data processing function.
#Feature :
1.performance timing: Measures precise execution time using time.perf_counter().
2.Automated logging: Logs start times,success durations and detailed errorsusing pythons built in logging module.
3.Rebust exception handling: Capture runtime errors, logs them and safely re raises time to prevent silent failures.

Usage example:
heres how you can use the ai tememetry decorator in your functions:
@ai_telemetry:
def simulate_ai_model_training(epochs:int,batch_size:int)->str:
   time.sleep(1.5)
   if epochs <= 0:
     raise ValueError("Number of epochs must be greater than zero")
   return f"model trained successfully for {epochs}epochs and batch size {batch_size}"

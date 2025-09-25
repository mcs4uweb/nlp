import time
from typing import Any, Callable
from datetime import datetime

class RepeatFunctionWithDelay:
    def __init__(self):
        self.start_time = None
        self.iteration_count = 0

    def initialize(self, iterations: int = None, total_time: float = None, delay: float = 1.0, 
            target_condition: Callable[[Any], bool] = None
        ):
        self.iterations = iterations
        self.total_time = total_time
        self.delay = delay
        self.target_condition = target_condition
        self.last_result = None
    
    def run(self, func: Callable, *args, **kwargs):
        """
        Execute the provided function in a loop with variable arguments.
        Break if iterations, total time or target condition is matched.
        
        Args:
            func: Function to be called
            *args: Variable positional arguments to pass to the function
            **kwargs: Variable keyword arguments to pass to the function
        """
        self.start_time = time.time()
        self.iteration_count = 0
        
        while True:
            if self.iterations is not None and self.iteration_count >= self.iterations:
                print("Reached maximum iterations")
                break
                
            if self.total_time is not None and (time.time() - self.start_time) >= self.total_time:
                print("Reached time limit")
                break
                
            time.sleep(self.delay)
            
            # Call function with all provided arguments
            try:
                self.last_result = func(*args, **kwargs)
            except Exception as e:
                self.last_result = e
                print(f"Error running function: {str(e)}")

            # Check if target condition is met
            if self.target_condition is not None:
                try:
                    if self.target_condition(self.last_result):
                        print("Target condition met")
                        break
                except Exception as e:
                    print(f"Error evaluating target condition: {str(e)}")

            self.iteration_count += 1
    
    @property
    def elapsed_time(self) -> float:
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time
    
    @property
    def remaining_iterations(self) -> int:
        if self.iterations is None:
            return float('inf')
        return max(0, self.iterations - self.iteration_count)
    
    @property
    def result(self) -> Any:
        return self.last_result
    
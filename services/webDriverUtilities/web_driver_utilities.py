from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import time
def retryOperation(maxAttempts=5, delay=1):
    def decoratorRetry(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < maxAttempts:
                try:
                    return func(*args, **kwargs)
                except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
                    funcName = func.__name__
                    print(f"Attempt {attempts + 1} of {maxAttempts} on {funcName} failed: {e}")
                    time.sleep(delay)
                    attempts += 1
                    if attempts == maxAttempts:
                        raise
        return wrapper
    return decoratorRetry
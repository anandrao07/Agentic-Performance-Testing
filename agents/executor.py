import time
import random


class Executor:
    def __init__(self):
        self.name = "Performance Test Executor"

    def run_test(self, test_name="default_test"):
        print(f"[EXECUTOR] Running test: {test_name}")

        # Simulate test execution time
        time.sleep(2)

        # Simulated test results
        result = {
            "test_name": test_name,
            "avg_response_time_ms": random.randint(200, 800),
            "error_rate": round(random.uniform(0, 5), 2),
            "status": "PASS"
        }

        print(f"[EXECUTOR] Test completed: {result}")
        return result

class DecisionEngine:
    def __init__(self, max_retries=2):
        self.max_retries = max_retries

    def decide(self, analysis, attempt):
        status = analysis["status"]

        if status == "PASS":
            return {
                "action": "SUCCESS",
                "message": "System healthy. No action required."
            }

        if status in ["WARNING", "FAIL"]:
            if attempt < self.max_retries:
                return {
                    "action": "RETRY",
                    "message": f"Issue detected. Retrying test (attempt {attempt + 1})."
                }
            else:
                return {
                    "action": "ESCALATE",
                    "message": "Max retries reached. Escalating issue."
                }

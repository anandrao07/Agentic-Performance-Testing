import yaml


class Analyzer:
    def __init__(self, config_path="configs/test_config.yaml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        self.max_response_time = config["thresholds"]["max_response_time_ms"]
        self.max_error_rate = config["thresholds"]["max_error_rate"]

    def analyze(self, test_result):
        avg_time = test_result["avg_response_time_ms"]
        error_rate = test_result["error_rate"]

        analysis = {
            "status": "PASS",
            "issues": []
        }

        if avg_time > self.max_response_time:
            analysis["status"] = "WARNING"
            analysis["issues"].append(
                f"Response time {avg_time}ms exceeds threshold {self.max_response_time}ms"
            )

        if error_rate > self.max_error_rate:
            analysis["status"] = "FAIL"
            analysis["issues"].append(
                f"Error rate {error_rate}% exceeds threshold {self.max_error_rate}%"
            )

        return analysis

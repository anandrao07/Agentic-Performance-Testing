class Reporter:
    def generate_report(self, test_result, analysis):
        report = {
            "test_name": test_result["test_name"],
            "summary": "",
            "details": {
                "avg_response_time_ms": test_result["avg_response_time_ms"],
                "error_rate": test_result["error_rate"]
            }
        }

        if analysis["status"] == "PASS":
            report["summary"] = "System performance is within acceptable limits."
        elif analysis["status"] == "WARNING":
            report["summary"] = "Performance degradation detected. Review recommended."
        else:
            report["summary"] = "Critical performance issues detected. Immediate action required."

        return report

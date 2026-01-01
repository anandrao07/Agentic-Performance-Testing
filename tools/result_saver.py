import json
import os
from datetime import datetime


class ResultSaver:
    def save(self, test_name, report):
        os.makedirs("data/processed", exist_ok=True)

        filename = f"data/processed/{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, "w") as f:
            json.dump(report, f, indent=4)

        print(f"[INFO] Results saved to {filename}")

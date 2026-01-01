# orchestrator.py
from agents.executor import Executor
from agents.analyzer import Analyzer
from agents.reporter import Reporter
from agents.decision_engine import DecisionEngine
from agents.reasoner import Reasoner
from tools.result_saver import ResultSaver
import time

class Orchestrator:
    def __init__(self):
        self.executor = Executor()
        self.analyzer = Analyzer()
        self.reporter = Reporter()
        self.decision_engine = DecisionEngine()
        self.reasoner = Reasoner()
        self.saver = ResultSaver()
        self.max_attempts = 3

    def start(self):
        print("[INFO] Starting performance test with reasoning and self-healing...")

        attempt = 1
        while attempt <= self.max_attempts:
            print(f"\n[INFO] Test Attempt #{attempt}")

            # Execute test
            result = self.executor.run_test("login_load_test")
            analysis = self.analyzer.analyze(result)
            report = self.reporter.generate_report(result, analysis)

            # Reasoning
            explanation = self.reasoner.explain(result, analysis)
            report["explanation"] = explanation

            # Decision making (retry/escalate)
            decision = self.decision_engine.decide(analysis, attempt)

            # Save results
            self.saver.save(result["test_name"], {
                "attempt": attempt,
                "report": report,
                "decision": decision
            })

            print(f"[DECISION] {decision['message']}")
            print(f"[REASONING] {explanation}")

            if decision["action"] == "SUCCESS":
                break
            elif decision["action"] == "ESCALATE":
                print("[ALERT] Max retries reached. Escalation triggered.")
                break

            # Wait before retry
            print("[INFO] Retrying after delay...\n")
            time.sleep(2)
            attempt += 1

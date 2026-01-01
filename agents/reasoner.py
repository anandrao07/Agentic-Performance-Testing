import openai

class Reasoner:
    def __init__(self, api_key=None):
        # You can set OPENAI_API_KEY as environment variable
        self.api_key = api_key
        if api_key:
            openai.api_key = api_key

    def explain(self, test_result, analysis):
        """
        Generates a natural language explanation of performance results.
        """
        prompt = f"""
        You are a performance testing expert.
        Analyze the following test results and give a concise explanation:

        Test Result: {test_result}
        Analysis: {analysis}

        Explain in human-readable terms what happened, why it might have happened,
        and possible actions to take.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=200
            )
            explanation = response['choices'][0]['message']['content'].strip()
            return explanation

        except Exception as e:
            return f"[ERROR] Reasoning failed: {e}"

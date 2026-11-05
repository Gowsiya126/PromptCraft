class PromptEvaluator:

    def evaluate(self, improved_prompt):

        # Convert prompt to lowercase for checking
        prompt = improved_prompt.lower()

        # Check important prompt elements
        checks = {
            "Role": "role:" in prompt,
            "Context": "context:" in prompt,
            "Instructions": "instructions:" in prompt,
            "Audience": "audience:" in prompt,
            "Constraints": "constraints:" in prompt,
            "Output Format": "output format:" in prompt
        }

        # Count completed checks
        passed = sum(checks.values())
        total = len(checks)

        # Calculate quality score
        score = round((passed / total) * 100)

        # Give feedback
        if score == 100:
            quality = "Excellent"
            feedback = "The prompt contains all important elements."
        elif score >= 70:
            quality = "Good"
            feedback = "The prompt is well structured, but a few elements are missing."
        elif score >= 40:
            quality = "Needs Improvement"
            feedback = "The prompt needs more structure and detail."
        else:
            quality = "Poor"
            feedback = "The prompt is missing several important elements."

        return {
            "score": score,
            "quality": quality,
            "checks": checks,
            "feedback": feedback
        }
import re


class PromptAnalyst:

    def analyze(self, user_input):

        # Check whether the user entered something
        if not user_input or not user_input.strip():
            return {
                "status": "error",
                "message": "Please enter a prompt."
            }

        prompt = user_input.strip()

        # Identify the main topic
        words = prompt.split()

        # Check prompt length
        word_count = len(words)

        # Identify useful prompt elements
        role_words = ["act as", "you are", "behave as"]
        context_words = ["context", "background", "student", "beginner"]
        constraint_words = ["only", "under", "within", "limit", "avoid"]
        output_words = ["format", "table", "list", "bullet", "report"]

        lower_prompt = prompt.lower()

        has_role = any(word in lower_prompt for word in role_words)
        has_context = any(word in lower_prompt for word in context_words)
        has_constraints = any(word in lower_prompt for word in constraint_words)
        has_output_format = any(word in lower_prompt for word in output_words)

        # Identify missing elements
        missing = []

        if not has_role:
            missing.append("Role")
        if not has_context:
            missing.append("Context")
        if not has_constraints:
            missing.append("Constraints")
        if not has_output_format:
            missing.append("Output format")

        # Recommend techniques
        techniques = ["Direct Prompting"]

        if not has_role:
            techniques.append("Role Prompting")

        if not has_context:
            techniques.append("Context Prompting")

        if not has_constraints:
            techniques.append("Constraint Prompting")

        if not has_output_format:
            techniques.append("Output Format Prompting")

        # Return analysis
        return {
            "status": "success",
            "original_prompt": prompt,
            "word_count": word_count,
            "missing_elements": missing,
            "recommended_techniques": techniques,
            "clarity": "Needs improvement" if missing else "Well structured"
        }
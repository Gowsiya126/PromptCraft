class PromptOptimizer:

    def optimize(self, improved_prompt, evaluation):

        optimized_prompt = improved_prompt
        changes_made = []

        # Read evaluator results
        checks = evaluation["checks"]

        # Add missing sections if required
        if not checks.get("Role", False):
            optimized_prompt += "\n\nROLE:\nAct as an expert in the requested topic."
            changes_made.append("Added Role section.")

        if not checks.get("Context", False):
            optimized_prompt += "\n\nCONTEXT:\nUnderstand the user's background and requirements."
            changes_made.append("Added Context section.")

        if not checks.get("Instructions", False):
            optimized_prompt += "\n\nINSTRUCTIONS:\nComplete the requested task clearly and accurately."
            changes_made.append("Added Instructions section.")

        if not checks.get("Audience", False):
            optimized_prompt += "\n\nAUDIENCE:\nAssume the reader is a beginner."
            changes_made.append("Added Audience section.")

        if not checks.get("Constraints", False):
            optimized_prompt += "\n\nCONSTRAINTS:\nAvoid unnecessary complexity and irrelevant information."
            changes_made.append("Added Constraints section.")

        if not checks.get("Output Format", False):
            optimized_prompt += "\n\nOUTPUT FORMAT:\nUse clear headings and bullet points."
            changes_made.append("Added Output Format section.")

        # Add extra quality improvements
        if "SUCCESS CRITERIA:" not in optimized_prompt.upper():

            optimized_prompt += """

SUCCESS CRITERIA:
- Answer the user's actual question.
- Provide accurate and relevant information.
- Use clear explanations and practical examples.
"""

            changes_made.append("Added Success Criteria.")

        if not changes_made:
            changes_made.append("Prompt structure is already strong.")

        return {
            "optimized_prompt": optimized_prompt,
            "changes_made": changes_made,
            "total_improvements": len(changes_made)
        }
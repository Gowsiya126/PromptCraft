class PromptArchitect:

    def build_prompt(self, analysis):

        # Get the original user prompt
        original = analysis["original_prompt"]

        # Get missing elements
        missing = analysis["missing_elements"]

        # Create a structured prompt
        improved_prompt = f"""
ROLE:
Act as an experienced subject matter expert and helpful teacher.

CONTEXT:
The user needs help with the following task:
{original}

AUDIENCE:
Assume the user is a beginner unless otherwise specified.

INSTRUCTIONS:
1. Understand the user's original request.
2. Explain the topic clearly.
3. Use simple and practical examples.
4. Break complex ideas into smaller steps.

CONSTRAINTS:
- Avoid unnecessary technical jargon.
- Keep the explanation beginner-friendly.
- Do not go beyond the requested topic.

OUTPUT FORMAT:
- Use clear headings.
- Use bullet points.
- Include practical examples.
- Present the answer step by step.

ORIGINAL PROMPT:
{original}

MISSING ELEMENTS IDENTIFIED:
{', '.join(missing) if missing else 'None'}
"""

        return {
            "original_prompt": original,
            "improved_prompt": improved_prompt.strip(),
            "techniques_used": [
                "Direct Prompting",
                "Role Prompting",
                "Context Prompting",
                "Constraint Prompting",
                "Output Format Prompting",
                "Step-by-step Prompting",
                "Persona Prompting"
            ]
        }
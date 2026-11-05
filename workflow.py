from agents.prompt_analyst import PromptAnalyst
from agents.prompt_architect import PromptArchitect
from agents.prompt_evaluator import PromptEvaluator
from agents.prompt_optimizer import PromptOptimizer


class PromptCraftWorkflow:

    def __init__(self):
        self.analyst = PromptAnalyst()
        self.architect = PromptArchitect()
        self.evaluator = PromptEvaluator()
        self.optimizer = PromptOptimizer()

    def run(self, user_prompt):

        # Agent 1: Analyze
        analysis = self.analyst.analyze(user_prompt)

        if analysis["status"] == "error":
            return analysis

        # Agent 2: Architect
        architecture = self.architect.build_prompt(analysis)

        # Agent 3: Evaluate
        first_evaluation = self.evaluator.evaluate(
            architecture["improved_prompt"]
        )

        # Agent 4: Optimize
        optimization = self.optimizer.optimize(
            architecture["improved_prompt"],
            first_evaluation
        )

        # Evaluate optimized prompt again
        final_evaluation = self.evaluator.evaluate(
            optimization["optimized_prompt"]
        )

        return {
            "status": "success",
            "original_prompt": user_prompt,
            "analysis": analysis,
            "improved_prompt": architecture["improved_prompt"],
            "optimized_prompt": optimization["optimized_prompt"],
            "techniques_used": architecture["techniques_used"],
            "first_evaluation": first_evaluation,
            "final_evaluation": final_evaluation,
            "changes_made": optimization["changes_made"]
        }


if __name__ == "__main__":

    workflow = PromptCraftWorkflow()

    print("\n========== PROMPTCRAFT STUDIO ==========")

    user_input = input("\nEnter your prompt: ")

    result = workflow.run(user_input)

    if result["status"] == "success":

        print("\n===== ORIGINAL PROMPT =====")
        print(result["original_prompt"])

        print("\n===== ANALYSIS =====")
        print("Missing elements:",
              result["analysis"]["missing_elements"])

        print("\n===== OPTIMIZED PROMPT =====")
        print(result["optimized_prompt"])

        print("\n===== FIRST EVALUATION =====")
        print(result["first_evaluation"]["score"], "/ 100")

        print("\n===== FINAL EVALUATION =====")
        print(result["final_evaluation"]["score"], "/ 100")

        print("\n===== IMPROVEMENTS =====")
        for change in result["changes_made"]:
            print("-", change)

        print("\n===== PROMPTCRAFT COMPLETED =====")

    else:
        print("Error:", result["message"])
PROMPT_TECHNIQUES = {

    "Direct Prompting":
        "Give a clear and direct instruction.",

    "Role Prompting":
        "Assign a specific expert role to the AI.",

    "Context Prompting":
        "Provide background information and relevant context.",

    "Constraint Prompting":
        "Set clear limits, rules and restrictions.",

    "Output Format Prompting":
        "Specify the required response format.",

    "Step-by-Step Prompting":
        "Break the task into smaller logical steps.",

    "Zero-Shot Prompting":
        "Ask the AI to complete a task without examples.",

    "One-Shot Prompting":
        "Provide one example to guide the response.",

    "Few-Shot Prompting":
        "Provide multiple examples to guide the response.",

    "Chain Prompting":
        "Divide a complex task into connected prompts.",

    "Persona Prompting":
        "Give the AI a particular personality or communication style.",

    "Iterative Prompting":
        "Improve the response through repeated feedback.",

    "Comparative Prompting":
        "Compare multiple options using common criteria."
}


def get_all_techniques():

    return PROMPT_TECHNIQUES


def get_technique_count():

    return len(PROMPT_TECHNIQUES)
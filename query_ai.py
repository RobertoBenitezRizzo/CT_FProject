import openai
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

openai.api_key = config["api_key"]

def generate_cfg(prompt):
    """Query the AI tool to generate CFG for a given prompt."""
    response = openai.ChatCompletion.create(
        model=config["model"],
        messages=[
            {"role": "system", "content": "Generate CFG rules for syntax validation."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    # Example usage
    prompt = "Generate CFG rules for arithmetic expressions."
    cfg_rules = generate_cfg(prompt)
    print("Generated CFG:\n", cfg_rules)

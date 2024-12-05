import json

def evaluate(cfg_rules, test_cases):
    """Evaluate CFG rules against a set of test cases."""
    passed = 0
    total = len(test_cases)

    for case in test_cases:
        # Simulate validation (mock logic; replace with actual parser logic)
        if case["input"] in cfg_rules.get(case["construct"], {}).values():
            passed += 1
        else:
            print(f"Failed case: {case['input']}")

    accuracy = (passed / total) * 100
    print(f"Evaluation completed: {accuracy}% accuracy")
    return accuracy

if __name__ == "__main__":
    # Load CFG rules
    with open("../cfg_rules/hardcoded_rules.json", "r") as rules_file:
        cfg_rules = json.load(rules_file)

    # Load test cases
    with open("test_cases/arithmetic_tests.json", "r") as tests_file:
        test_cases = json.load(tests_file)

    # Run evaluation
    evaluate(cfg_rules, test_cases)

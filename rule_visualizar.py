import json
from graphviz import Digraph

def visualize_cfg(cfg_rules, construct_name):
    """Visualize CFG rules using Graphviz."""
    dot = Digraph(comment=f"CFG for {construct_name}")
    rules = cfg_rules.get(construct_name, {})

    for key, productions in rules.items():
        for production in productions:
            dot.edge(key, production)

    dot.render(f"output/{construct_name}_CFG", format="png")
    print(f"Visualization saved to output/{construct_name}_CFG.png")

if __name__ == "__main__":
    with open("hardcoded_rules.json", "r") as file:
        cfg_rules = json.load(file)
    visualize_cfg(cfg_rules, "arithmetic_expressions")

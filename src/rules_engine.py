import pandas as pd
import json
import os

def evaluate_condition(value, condition):
    """
    Evaluate a numeric condition like '> 90' or '< 70' against a value.
    """
    operator, threshold = condition.split()
    threshold = float(threshold)
    value = float(value)

    if operator == ">":
        return value > threshold
    elif operator == "<":
        return value < threshold
    else:
        return False

def apply_rules(vitals_df, labs_df, rules):
    """
    Apply CDS rules to vitals and labs data.
    Returns a list of alert dictionaries.
    """
    alerts = []

    # Vitals-based rules
    for _, row in vitals_df.iterrows():
        for rule_name, rule_set in rules.items():
            triggered = []

            for variable, condition in rule_set.items():
                if variable in row.index:
                    if evaluate_condition(row[variable], condition):
                        triggered.append(variable)

            if triggered:
                alerts.append({
                    "timestamp": row["timestamp"],
                    "source": "vitals",
                    "rule": rule_name,
                    "triggered_on": ";".join(triggered)
                })

    # Labs-based rules
    for _, row in labs_df.iterrows():
        for rule_name, rule_set in rules.items():
            triggered = []

            for variable, condition in rule_set.items():
                if variable in row.index:
                    if evaluate_condition(row[variable], condition):
                        triggered.append(variable)

            if triggered:
                alerts.append({
                    "timestamp": row["timestamp"],
                    "source": "labs",
                    "rule": rule_name,
                    "triggered_on": ";".join(triggered)
                })

    return alerts

if __name__ == "__main__":
    # Assume script is run from repo root
    vitals_path = os.path.join("data", "patient_vitals.csv")
    labs_path = os.path.join("data", "patient_labs.csv")
    rules_path = os.path.join("rules", "cds_rules.json")

    vitals = pd.read_csv(vitals_path)
    labs = pd.read_csv(labs_path)

    with open(rules_path) as f:
        rules = json.load(f)

    alerts = apply_rules(vitals, labs, rules)

    alerts_df = pd.DataFrame(alerts)
    alerts_df.to_csv("alerts_output.csv", index=False)

    print("Alerts generated:")
    print(alerts_df)

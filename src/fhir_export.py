import json
import pandas as pd

def create_fhir_detected_issue(rule_name, timestamp, details):
    """
    Build a simple FHIR DetectedIssue resource as a Python dict.
    """
    return {
        "resourceType": "DetectedIssue",
        "status": "final",
        "code": {
            "text": f"CDS Alert: {rule_name}"
        },
        "detail": f"Triggered on: {', '.join(details)}",
        "identifiedDateTime": timestamp
    }

# Load alerts produced by rules_engine.py
alerts_df = pd.read_csv("alerts_output.csv")

bundle = {
    "resourceType": "Bundle",
    "type": "collection",
    "entry": []
}

for _, row in alerts_df.iterrows():
    triggered_list = str(row["triggered_on"]).split(";")
    triggered_list = [item for item in triggered_list if item]

    resource = create_fhir_detected_issue(
        rule_name=row["rule"],
        timestamp=row["timestamp"],
        details=triggered_list
    )

    bundle["entry"].append({"resource": resource})

with open("fhir_detected_issues.json", "w") as f:
    json.dump(bundle, f, indent=4)

print("FHIR DetectedIssue bundle created: fhir_detected_issues.json")

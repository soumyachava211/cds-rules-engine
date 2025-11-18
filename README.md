# Clinical Decision Support (CDS) Rules Engine

A Python-based Clinical Decision Support (CDS) rules engine that evaluates patient vitals and lab values using JSON-configurable rules and generates standardized FHIR `DetectedIssue` alerts. This project simulates real EHR alerting workflows using only synthetic data.

---

## 🚀 Features

- Rule-based evaluation of patient vitals and labs
- JSON-configurable CDS rules
- Alerts for:
  - Sepsis/SIRS indicators
  - Hyperglycemia & hypoglycemia
  - Hypertension
  - Tachycardia / bradycardia
  - Fever
  - Low oxygen saturation
- FHIR `DetectedIssue` bundle export
- Simple, readable Python code
- Ready-to-run demo with sample data

---

## 📂 Project Structure

```text
cds-rules-engine/
├── data/
│   ├── patient_vitals.csv
│   └── patient_labs.csv
├── rules/
│   └── cds_rules.json
├── src/
│   ├── rules_engine.py
│   └── fhir_export.py
├── notebooks/
│   └── (optional demo notebook)
├── alerts_output.csv          # generated after running rules_engine.py
├── fhir_detected_issues.json  # generated after running fhir_export.py
└── requirements.txt

▶️ How to Run

Install dependencies:

pip install -r requirements.txt

Run the rules engine:

python src/rules_engine.py

This will create alerts_output.csv.


Export FHIR DetectedIssue bundle:

python src/fhir_export.py

This will create fhir_detected_issues.json.

🧠 Skills Demonstrated

Clinical decision support (CDS) logic

Rule-based reasoning over vitals and labs

JSON-based configuration of clinical rules

FHIR resource modeling (DetectedIssue, Bundle)

Python data processing (Pandas)

Synthetic healthcare data handling

🔒 Notes

All data in this repository is synthetic and for educational/demonstration purposes only.

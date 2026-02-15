# Rockwell AI Governance Prototype
Teaching Gen AI how to be a Team Member
🎯 Overview
This project establishes a Governance & Safety Framework for integrating Large Language Models (LLMs), specifically GitHub Copilot, into industrial software development environments. The goal is to transform AI from a generic code generator into a reliable Junior Team Member that adheres to Rockwell Automation’s safety, architectural, and documentation standards.
🛠 Features
• Deterministic AI Guardrails: System-level instructions that enforce strict coding patterns.
• Automated Safety Validation: Integration with pytest to catch logic errors that could impact physical hardware.
• Hallucination Mitigation: Grounding AI responses in specific industrial contexts to prevent the use of non-existent libraries.
• Fail-Safe Logic Design: Patterns that ensure systems default to a secure state upon sensor or communication failure.
🏗 Project Structure
rockwell-ai-governance/
├── .github/
│   └── copilot-instructions.md  <-- The "Rules of Governance"
├── src/
│   ├── sensor_reader.py         <-- Industrial sensor simulation
│   └── safety_protocols.py      <-- Fail-safe logic implementation
├── tests/
│   ├── test_sensor.py           <-- Unit tests for boundary validation
│   └── stress_test.py           <-- AI-generated code stress testing
├── README.md
└── requirements.txt

🚦 Governance & Safety Rules
The framework enforces the following standards through .github/copilot-instructions.md:
1. Type Safety: All Python functions must include Type Hints.
2. Documentation: Strict adherence to Google-Style Docstrings.
3. Boundary Validation: Every input must be sanitized against predefined industrial ranges (e.g., SENS- ID prefix).
4. Defensive Programming: Mandatory try-except blocks for all hardware-simulating functions.

🧪 Testing & Validation
The project uses pytest to ensure that even if the AI suggests a solution, it passes our safety thresholds.
Safety Boundary Test
Validates that telemetry data never exceeds critical physical limits:


def test_sensor_safety_boundary():
    result = read_industrial_sensor("SENS-01")
    if result is not None:
        assert result <= 100.0  # Critical Safety Limit

How to run tests:

python -m pytest tests/test_sensor.py

📈 Key Findings (The "101.4°C" Case)
During development, a stress test identified a Critical Security Violation where the AI-generated telemetry returned 101.4°C.
• Result: The test suite successfully blocked the execution.
• Lesson: This proves that Automated Guardrails are essential to prevent AI hallucinations from affecting industrial safety.

🚀 Future Roadmap
• RAG Integration: Connecting the framework to official Rockwell manuals (PDFs/Wikis).
• Multi-language Support: Expanding governance rules to C++ and Go.
• Automated PR Reviewer: Using AI to flag code that violates safety conventions.
Author: Oskar Vanegas
Role: AI Governance & Software Safety Intern (Candidate)
Company: Rockwell Automation Internship Program FY26


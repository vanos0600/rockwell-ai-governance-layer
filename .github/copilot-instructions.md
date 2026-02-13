# Rockwell Automation - AI Coding Standards & Governance

## 1. Safety & Operational Reliability
- **Strict Exception Handling:** NEVER use bare `except:` blocks. All exceptions must be specific (e.g., `ValueError`, `ConnectionError`) to ensure traceability in industrial logs.
- **Fail-Safe Design:** Functions interacting with hardware or sensors must implement a fail-safe mechanism. On failure, return `None` or a safe default value to prevent cascading system failures.
- **Input Validation:** All industrial IDs and telemetry data must be sanitized and validated before processing (e.g., checking for 'SENS-' prefixes).

## 2. Technical Standards (Python 3.10+)
- **Mandatory Type Hinting:** Use explicit type hints for all function signatures and complex variables to ensure type safety and improve AI context.
- **Documentation:** All functions must include Google-Style Docstrings explaining Args, Returns, and potential Raises.
- **Modular Logic:** Decouple sensor reading logic from business logic to facilitate unit testing and hardware hardware emulation (mocking).

## 3. AI Collaboration Principles
- **Context Awareness:** Copilot must prioritize the safety boundaries defined in the project's test suite (e.g., 100°C limit).
- **Code Review Readiness:** AI-generated code must be optimized for human readability and peer review.
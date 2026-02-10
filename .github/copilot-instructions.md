# 🤖 Rockwell Automation - AI Coding Standards
## 1. 🛡️ Safety & Reliability
- **Error Handling:** NEVER leave bare `except:` blocks.
- **Fail-Safe:** Sensors must return None or safe defaults on failure.
## 2. 🐍 Style
- **Type Hinting:** Mandatory Python 3.10+ hints.
- **Docstrings:** Google-Style required.
Based on your Rockwell Automation coding standards document, you must follow:

**Safety & Reliability:**
- Avoid bare `except:` blocks - always specify exception types
- Sensors must return `None` or safe defaults when they fail

**Style:**
- Use Python 3.10+ type hints (mandatory)
- Write Google-style docstrings

These standards ensure your code is safe, maintainable, and reliable for industrial automation contexts.
# Project TITAN Setup Guide

## Prerequisites

Before running Project TITAN, install the following software:

| Software | Version |
|-----------|---------|
| Python | 3.11+ |
| Git | Latest |
| VS Code | Latest |
| Microsoft Fabric | Trial / Capacity |
| Power BI Desktop | Latest |

---

# Clone Repository

```bash
git clone https://github.com/Janak2026/project-titan.git

cd project-titan
```

---

# Create Virtual Environment

```bash
python -m venv .venv
```

---

# Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Structure

```
project-titan/

docs/

data/

ai/

powerbi/

src/

tests/
```

---

# Configuration

Update configuration values inside:

```
src/config/config.py
```

Example:

```python
FABRIC_WORKSPACE = ""

LAKEHOUSE_NAME = ""

OPENAI_ENDPOINT = ""

OPENAI_API_KEY = ""

MODEL_NAME = ""
```

---

# Running the Project

Project TITAN is developed module by module.

Typical execution order:

1. Data Ingestion
2. Bronze Layer
3. Silver Layer
4. Gold Layer
5. Machine Learning
6. RAG Pipeline
7. AI Agent
8. Power BI

---

# Verify Installation

Run:

```bash
python --version
```

```bash
pip list
```

If no errors occur, the environment is ready.

---

# Troubleshooting

Common issues:

- Python not added to PATH
- Git not installed
- Missing Python packages
- Fabric workspace not configured

---

# Next Steps

After setup is complete:

- Configure Microsoft Fabric
- Create Lakehouse
- Execute ingestion pipeline
- Build Medallion Architecture
- Train ML models
- Build RAG pipeline
- Develop AI Agent
- Publish Power BI dashboards
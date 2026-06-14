# SentinelTrapAI: Autonomous AI Honeypot & Threat Logging System Backend

SentinelTrapAI is an asynchronous, headless network decoy infrastructure engineered to monitor, capture, and log unauthorized connection anomalies and malicious payloads. By simulating open vulnerable systems (Honeypots), the application misdirects threat vectors inside institutional networks while actively gathering forensic telemetry data.

Constructed entirely as a headless engine, developer validation and operational analytics run natively through automated backend documentation specifications, bypassing unnecessary frontend UI overhead.

---

## 🛠️ Core Technology Stack

- **Integrated Development Environment:** Visual Studio Code (VS Code)
- **Application Core:** Python FastAPI (Asynchronous ASGI framework for non-blocking route handling)
- **Database Architecture:** MongoDB Community Server (NoSQL storage running locally on port `27017`)
- **Object-Document Mapper (ODM):** Beanie ODM (Enforces structural Pydantic validation over loose documents)
- **Database Drivers:** Motor v3.3.2 & PyMongo v4.6.3 (Synchronized versions matching async lifecycle loops)

---

## 📊 Relational Schema Modeling in NoSQL

While MongoDB is a NoSQL database storing fluid BSON documents, this architecture implements an advanced **Document Referencing (Normalization)** schema map using Beanie `Link[]` definitions to track corporate assets securely:

- **Departments Module (One-to-Many):** Models network zones (e.g., `"Simulation Lab"`) maintaining distinct threat thresholds.
- **Attackers Module (One-to-Many):** Tracks malicious client footprints, recording remote IP addresses and country locations.
- **Alerts Module (Many-to-One):** Automatically intercepts simulated exploit events, storing references back to the target department and root attacker using system hexadecimal `_id` pointers.
- **Incidents & Forensic Reports:** Handles macro security investigations linked directly to heavy payload strings.

---

## 🚀 Local Installation & Execution

### 1. Verification of Prerequisites
Ensure **MongoDB Community Server** is installed on your operating system and running cleanly as a background service.

### 2. Isolate and Activate the Workspace
Open your VS Code terminal and isolate your package bindings using the native Windows PowerShell execution policy:
```powershell
& ".\honeypot_system\venv\Scripts\Activate.ps1"

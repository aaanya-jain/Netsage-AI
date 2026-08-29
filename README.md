# Netsage AI 
NetSage AI is an AI-assisted network troubleshooting project designed for Cisco Packet Tracer and networking lab scenarios.

The system analyzes network symptoms, topology notes, and show-command outputs to suggest the most likely root cause, OSI layer, supporting evidence, next troubleshooting command, and possible fix.

A human reviewer must always verify the AI diagnosis before accepting the solution.

Features
30 troubleshooting cases covering:
VLAN
Gateway
DHCP
DNS
Routing
ACL
NAT
Wireless
Interface problems
IP addressing
Gemini AI integration
Structured JSON-based diagnosis
Rule-based Python checker
Issue type and severity dashboard
Human review system
Responsible AI review log
Accepted, Edited, and Rejected diagnosis tracking
Project Structure
NetSage_AI/

data/
    cases.csv
    review_log.csv

docs/
    architecture.md
    audit_logs.md
    features.md
    Index.md
    Setup.md
    Usage.md

prompt/
    Diagonose_prompt.md

src/
    App.py
    Checker.py
    Engine.py

workflows/
    Pages.yml

README.md
requirements.txt
Installation

First install the required Python libraries.

pip install -r requirements.txt
Gemini API Key

The project requires a Gemini API key.

Set the API key as an environment variable.

Windows PowerShell
$env:GEMINI_API_KEY="your_gemini_api_key"
Windows Command Prompt
set GEMINI_API_KEY=your_gemini_api_key
macOS/Linux
export GEMINI_API_KEY="your_gemini_api_key"

Do not upload or publish your actual Gemini API key on GitHub.

Run the Project

From the main project folder, run:

streamlit run src/App.py

The Streamlit dashboard will open in your browser.

How the System Works
Select a troubleshooting case.
The rule-based checker checks common networking configuration problems.
Gemini analyzes the symptom and networking evidence.
Gemini returns:
Root cause
Confidence
OSI layer
Evidence
Next command
Fix steps
A human reviewer checks the AI response.
The reviewer marks the diagnosis as:
Accepted
Edited
Rejected
Responsible AI

AI-generated troubleshooting suggestions are not automatically accepted.

Every diagnosis requires human review. Incorrect or incomplete AI responses can be edited or rejected and documented in the review log.

Technology Used
Python
Streamlit
Pandas
Google Gemini API
CSV
Markdown
Purpose

The purpose of NetSage AI is to help junior network engineers understand how network symptoms and command outputs can be connected to likely root causes while keeping a human reviewer involved in the final troubleshooting decision.

# Architecture
NetSage AI uses four layers:
1. **Data**: CSV troubleshooting cases and human review logs.
2. **Deterministic checker**: Finds common patterns before/alongside AI.
3. **Gemini engine**: Sends structured case evidence to Gemini and expects JSON.
4. **Streamlit dashboard**: Shows issue trends, AI output, and mandatory human review.

Flow: Case → Rule Checker → Gemini Diagnosis → Human Accept/Edit/Reject → Review Log.

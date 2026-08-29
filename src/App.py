import os, sys, json
from pathlib import Path
import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from Engine import diagnose
from Checker import run_checks

st.set_page_config(page_title="NetSage AI", layout="wide")
st.title("NetSage AI — Network Troubleshooting with Human Review")
st.caption("AI suggestions are advisory. A human reviewer must approve, edit, or reject every diagnosis.")

cases = pd.read_csv(BASE / "data" / "cases.csv")
reviews = pd.read_csv(BASE / "data" / "review_log.csv")

c1, c2, c3 = st.columns(3)
c1.metric("Troubleshooting cases", len(cases))
c2.metric("Reviewed corrections", len(reviews))
c3.metric("Accepted/edited/rejected logged", reviews["review_status"].nunique())

st.subheader("Issue dashboard")
st.bar_chart(cases["concept_tag"].value_counts())
st.bar_chart(cases["severity"].value_counts())

case_id = st.selectbox("Select a case", cases["case_id"])
case = cases[cases.case_id == case_id].iloc[0].to_dict()
st.json(case)

combined = " ".join(str(v) for v in case.values())
st.subheader("Deterministic checker")
for item in run_checks(combined):
    st.write("•", item)

st.subheader("Gemini diagnosis")
if st.button("Run AI diagnosis"):
    try:
        prompt = (BASE / "prompt" / "Diagonose_prompt.md").read_text(encoding="utf-8")
        result = diagnose(case, prompt)
        st.json(result)
        st.session_state["diagnosis"] = result
    except Exception as e:
        st.error(str(e))

st.subheader("Mandatory human review")
status = st.radio("Review decision", ["Accepted", "Edited", "Rejected"], horizontal=True)
notes = st.text_area("Reviewer notes / corrections")
if st.button("Record review for this session"):
    st.success(f"Human review recorded in this session: {status}. Notes: {notes or 'No notes provided.'}")

st.subheader("Responsible AI log")
st.dataframe(reviews, use_container_width=True)

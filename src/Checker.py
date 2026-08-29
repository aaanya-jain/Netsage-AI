import re

def run_checks(text):
    text = (text or "").lower()
    findings = []
    if "duplicate ip" in text or "same ip" in text:
        findings.append("Possible duplicate IP address conflict.")
    if "wrong mask" in text or "subnet mask" in text and "255.255" in text:
        findings.append("Check subnet mask against intended network.")
    if "gateway" in text and ("wrong" in text or "mismatch" in text):
        findings.append("Possible default-gateway mismatch.")
    if "administratively down" in text or "shutdown" in text:
        findings.append("Interface may be administratively down.")
    if "vlan" in text and ("does not exist" in text or "missing" in text):
        findings.append("Required VLAN may be missing.")
    if "show ip route" in text and ("absent" in text or "missing" in text):
        findings.append("Possible missing route.")
    return findings or ["No deterministic pattern matched; use AI diagnosis and human review."]

if __name__ == "__main__":
    sample = "show ip interface brief: administratively down; show ip route: remote network missing"
    for x in run_checks(sample):
        print("-", x)

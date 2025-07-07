
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="HEC PathWise", layout="centered")
st.title("🎓 HEC PathWise: Transfer Evaluation Tool")

st.markdown("Upload a transcript and select a degree program to evaluate transferable credits.")

programs = [
    "BA in Music", "BBA in Management", "BA: General Studies", "BS Maritime Tran Mgmt Security",
    "BS in Health Administration", "BA in Political Science", "BS in Computer Engr.Tech",
    "BA in Communication Studies", "BS in Computer Science", "BS Nutritional Sci. Dietetics",
    "BS in Kinesiology", "BS in Admin of Justice", "BS in Biomedical Science",
    "BA Radio Television and Film", "BA in Psychology", "BA in Social Work", "BS in Mathematics",
    "BS in Athletic Training", "BBA in Finance", "BBA in Marketing", "BA in Sociology",
    "BS in Aviation Science Mgmt", "BS in Health Information Mgmt", "BBA in Accounting",
    "BS-TD Educational Studies", "BS in Interdisciplinary Stud", "BS in Chemistry Undergraduate",
    "BS in Industrial Technology", "BS in Biology Undergraduate", "BA Entermnt Record Indust Mgmt",
    "BS in Health", "BBA in Mgmt Inform. Systems", "BA in Art", "BS in Electrical & Comp Engr.",
    "BS in Sports Management", "BA in Journalism", "BS in Elect. Engineering Tech", "BA in History",
    "BS in Respiratory Therapy", "BS in Environmental Health", "BA in English", "BS in Civil Engineering",
    "BS in TDS Business & Corp Svc", "BS in Clinical Lab Science", "BS in Human Serv Consumer Sci",
    "BSIT in Industrial Technology"
]

selected_program = st.selectbox("🎓 Select a Degree Program", programs)

uploaded_file = st.file_uploader("📄 Upload a Transcript (PDF)", type=["pdf"])

if uploaded_file and selected_program:
    st.success(f"Transcript uploaded and program selected: {selected_program}")
    st.markdown("🛠️ Simulated evaluation results:")

    # Simulated table
    data = {
        "Course": ["ENGL 1301", "MATH 1314", "HIST 1301", "PSYC 2301", "BIOL 2401"],
        "Credits": [3, 3, 3, 3, 4],
        "Grade": ["A", "B", "C", "F", "B"],
        "Transferable": ["Yes", "Yes", "Yes", "No", "Yes"],
        "Reason (if not transferable)": ["", "", "", "Grade too low (F)", ""]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Transfer GPA calculation
    gpa_scale = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    df["Points"] = df.apply(lambda row: gpa_scale[row["Grade"]] * row["Credits"] if row["Transferable"] == "Yes" else 0, axis=1)
    total_credits = df[df["Transferable"] == "Yes"]["Credits"].sum()
    total_points = df["Points"].sum()
    transfer_gpa = total_points / total_credits if total_credits > 0 else 0
    st.markdown(f"**🎯 Transfer GPA (based on accepted credits): {transfer_gpa:.2f}**")

    # CSV download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📤 Download Evaluation Report (CSV)", data=csv, file_name="pathwise_evaluation.csv", mime="text/csv")

st.markdown("---")
st.caption("Made with ❤️ by Annette Linders & HEC Partners • Powered by Echo")

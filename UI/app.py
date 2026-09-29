import streamlit as st
import requests
import json

st.title("Resume Screening Application")

uploaded_file = st.file_uploader("Upload the Resume (PDF)", type="pdf")

if uploaded_file is not None:
    st.write("File Uploaded Successfully!", uploaded_file.name)

    if st.button("Process Resume"):
        response = requests.post("http://127.0.0.1:8000/screening", files={"resume": uploaded_file})

        if response.status_code == 200:
            st.success("Resume processed successfully!")

            response_data = response.json()
   
            evaluation = json.loads(response_data)

            st.header("Candidate Evaluation")

            status = evaluation["application_status"]
            skill_match = evaluation["skill_match_percentage"]

            col1, col2 = st.columns(2)

            with col1:
                if status == "SELECTED":
                    st.success(f"Application Status: {status}")
                else:
                    st.error(f"Application Status: {status}")

            with col2:
                st.metric("Skill Match",f"{skill_match}%")

            st.subheader("Reason")

            st.write(evaluation["reason"])

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Key Strengths")

                for strength in evaluation["key_strengths"]:
                    st.write(f"• {strength}")

            with col2:
                st.subheader("Key Gaps")

                for gap in evaluation["key_gaps"]:
                    st.write(f"• {gap}")

            st.subheader("Skill Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Matched Skills**")

                for skill in evaluation["matched_skills"]:
                    st.write(f"✅ {skill}")

            with col2:
                st.write("**Unmatched Required Skills**")

                for skill in evaluation["unmatched_required_skills"]:
                    st.write(f"❌ {skill}")

            st.subheader("Experience Match")

            required_experience = evaluation["experience_required"]
            candidate_experience = evaluation["candidate_experience"]

            st.write(
                f"**Required Experience:** {required_experience} years"
            )

            st.write(
                f"**Candidate Experience:** {candidate_experience} years"
            )

            if candidate_experience >= required_experience:
                st.success("Experience requirement satisfied")
            else:
                st.error("Experience requirement not satisfied")
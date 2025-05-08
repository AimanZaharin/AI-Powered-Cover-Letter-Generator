# maybe add level of experience to the gpt model
# add more details to the cover letter
# add copy to clipboard for easy copy and paste

import streamlit as st
from backend import get_response, extract_resume, extract_text_from_pdf
import os

st.set_page_config(
    page_title = "Cover Letter Generator",
    page_icon = "✉️",
    layout = "wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About":"Created by Aiman Zaharin"
    }
)

st.title("Cover Letter Generator")

st.markdown("### 📄 Upload Resume")
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

st.markdown("### 👤 Personal Information")
name = st.text_input("Full Name", placeholder="e.g., John Doe")
email = st.text_input("Email Address", placeholder="e.g., john.doe@email.com")
phone_number = st.text_input("Phone Number", placeholder="e.g., +60 12 345 6789")

col1, col2, col3 = st.columns(3)
with col1:
    zip_code = st.text_input("Zip Code", placeholder="e.g., 10001")
with col2:
    city = st.text_input("City", placeholder="e.g., New York")
with col3:
    state = st.text_input("State", placeholder="e.g., NY")

st.markdown("### 💼 Job Information")
job_title = st.text_input("Job Title", placeholder="e.g., Data Scientist")
company_name = st.text_input("Company Name", placeholder="e.g., OpenAI")
job_description = st.text_area("Job Description", height=200, placeholder="Paste the job description here...")

years_of_experience = st.number_input(
    "Years of Experience", min_value=0, max_value=50, value=0, step=1
)

tone = st.selectbox(
    "Preferred Tone of the Cover Letter", 
    ["Formal", "Friendly", "Professional", "Sarcastic"]
)
parameters = [uploaded_file, name, email, phone_number,
              zip_code, city, state, job_title, company_name, job_description, years_of_experience, tone]

if parameters in parameters or not all(parameters) :
    submit_button = st.button("Generate Cover Letter", type="primary", disabled=True)
else:
    submit_button = st.button("Generate Cover Letter", type="primary")

if submit_button:
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    for file in os.listdir("uploads"):
        file_path = os.path.join("uploads", file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    with open(f"uploads/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())

    upload_path = f"uploads/{uploaded_file.name}"

    try:
        text = extract_text_from_pdf(upload_path)
        extracted_info = extract_resume(text)
        user_input = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "zip_code": zip_code,
            "city": city,
            "state": state,
            "job_title": job_title,
            "company_name": company_name,
            "job_description": job_description,
            "years_of_experience": years_of_experience,
            "tone": tone,
        }
        response = get_response(extracted_info, user_input)
        st.success("Cover Letter Generated Successfully!")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")


from fastapi import FastAPI, UploadFile
from PyPDF2 import PdfReader
from agents.resume_extractor import extract_resume_data
from agents.jd_extractor import extract_jd_data
from agents.candidate_evaluation import evaluate_candidate

def parse_pdf(file):
    reader = PdfReader(file)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text

app = FastAPI()

@app.post("/screening")
def screening(resume: UploadFile):
    resume_text = parse_pdf(resume.file)
    extracted_resume_details = extract_resume_data(resume_text)

    jd_text = ""
    with open("resources/sample_JD.pdf", "rb") as file:
        jd_text = parse_pdf(file)

    extracted_jd_details = extract_jd_data(jd_text)

    evaluation_result = evaluate_candidate(extracted_resume_details, extracted_jd_details)

    return evaluation_result

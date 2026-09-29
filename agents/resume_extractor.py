from ollama import chat
from prompts import RESUME_EXTRACTION_PROMPT

def extract_resume_data(resume_data):
    prompt = RESUME_EXTRACTION_PROMPT.format(resume_text = resume_data)
    response = chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "system", "content": prompt
            }
        ], think=False
    )
    return response.message.content

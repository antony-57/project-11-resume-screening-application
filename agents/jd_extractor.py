from ollama import chat
from prompts import JD_EXTRACTION_PROMPT

def extract_jd_data(text):
    prompt = JD_EXTRACTION_PROMPT.format(jd_text = text)
    response = chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "user", "content": prompt
            }
        ], think=False
    )
    return response.message.content
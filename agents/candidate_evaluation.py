from ollama import chat
from prompts import CANDIDATE_EVALUATION_PROMPT

def evaluate_candidate(candidate_details: str, jd:str):
    prompt = CANDIDATE_EVALUATION_PROMPT.format(resume_json = candidate_details, jd_json = jd)
    response = chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "user", "content": prompt
            }
        ], think=False
    )
    return response.message.content
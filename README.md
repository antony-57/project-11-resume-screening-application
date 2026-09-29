# Resume Screening Application

My first Generative AI project — a resume screening application that uses a
local Large Language Model (LLM) to extract information from resumes and job
descriptions and evaluate candidate suitability.

The application uses **Ollama with Qwen3.5 4B** locally, so the LLM runs on my
own machine instead of relying on a paid cloud API.

**Completed:** September 28, 2026

## Features

- Upload a resume as a PDF
- Extract structured candidate information using a local LLM
- Extract structured job-description information
- Compare the candidate against the job requirements
- Evaluate:
  - Application status (Selected / Rejected)
  - Skill match percentage
  - Matched skills
  - Unmatched required skills
  - Candidate strengths
  - Skill gaps
  - Experience match
  - Reason for the decision
- Display the evaluation through a Streamlit interface

## Architecture

```text
Resume PDF ──────────┐
                     ↓
              PDF Text Extraction
                     ↓
              Resume Extraction Agent
                     │
                     ├──────────────┐
                     ↓              ↓
                Resume Data      JD Data
                     │              │
                     └──────┬───────┘
                            ↓
                 Candidate Evaluation Agent
                            ↓
                    Screening Result
                            ↓
                       FastAPI
                            ↓
                       Streamlit
````

## Tech Stack

* Python
* FastAPI
* Streamlit
* Ollama
* Qwen3.5 4B
* PyPDF2
* Requests

## Local LLM

This project uses **Qwen3.5 4B through Ollama** as the local LLM.

The basic flow is:

```text
Python Application → Ollama → Qwen3.5 4B → Response
```

No OpenAI API or paid cloud LLM service is required for the current version.

Before running the application, Ollama must be installed and the required
Qwen model must be available locally.

## Running the Application

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI backend:

```bash
uvicorn main:app --reload
```

Then start the Streamlit interface:

```bash
streamlit run UI/app.py
```

Upload a resume through the Streamlit interface and process it against the
sample job description.

## Project Structure

```text
Project_11/
│
├── agents/
│   ├── candidate_evaluation.py
│   ├── jd_extractor.py
│   └── resume_extractor.py
│
├── resources/
│   └── sample_JD.pdf
│
├── UI/
│   └── app.py
│
├── main.py
├── prompts.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Limitations

This is an initial GenAI application and is intended primarily as a learning
and portfolio project.

The candidate evaluation is based on information extracted by the LLM and
should not be treated as a replacement for human hiring decisions.

The current version also requires resumes to be uploaded manually and uses a
single job description for screening.

## Future Improvements

A future version could automate the screening workflow by introducing a
centralized resume storage system and a listener component.

The planned flow would be:

```text
Resume Upload
      ↓
Resume Storage
      ↓
Storage Listener
      ↓
Resume Extraction Agent
      ↓
Candidate Evaluation Agent
      ↓
Screening Result
      ↓
Result Storage
```

The listener would continuously monitor the storage system for new resumes
and automatically trigger the screening pipeline when a new file is detected.

This would turn the current interactive application into a more automated,
event-driven resume screening system capable of processing multiple
applications without manually starting the screening process for each resume.

## Project Context

This is my **first Generative AI project**.

The goal of this project was not to build a complete production hiring
platform, but to understand the fundamentals of building an application
around a pretrained LLM, including local LLM inference, prompt engineering,
structured extraction, agent-based processing, API integration, and UI
integration.

The current version intentionally keeps the architecture simple as a
starting point for my Generative AI learning journey.



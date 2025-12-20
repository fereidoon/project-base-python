RESUME_SCHEMA = """{
  "personal": {
    "full_name": "",
    "job_title": "",
    "email": "",
    "phone": "",
    "location": "",
    "date_of_birth": "",
    "nationality": ""
  },
  "summary": "",
  "experience": [
    {
      "company": "",
      "position": "",
      "location": "",
      "start_date": "",
      "end_date": "",
      "is_current": false,
      "description": "",
      "technologies": []
    }
  ],
  "education": [
    {
      "institution": "",
      "degree": "",
      "field_of_study": "",
      "start_date": "",
      "end_date": "",
      "grade": "",
      "description": ""
    }
  ],
  "skills": {
    "technical": [],
    "soft": [],
    "tools": [],
    "languages": []
  },
  "projects": [
    {
      "name": "",
      "role": "",
      "description": "",
      "technologies": [],
      "link": ""
    }
  ],
  "certifications": [
    {
      "name": "",
      "issuer": "",
      "date": "",
      "credential_id": "",
      "link": ""
    }
  ],
  "publications": [
    {
      "title": "",
      "publisher": "",
      "date": "",
      "link": ""
    }
  ],
  "languages": [
    {
      "name": "",
      "level": ""
    }
  ],
  "awards": [
    {
      "title": "",
      "issuer": "",
      "date": "",
      "description": ""
    }
  ],
  "volunteering": [
    {
      "organization": "",
      "role": "",
      "start_date": "",
      "end_date": "",
      "description": ""
    }
  ],
  "links": [
    {
      "type": "linkedin | github | portfolio | website | other",
      "url": ""
    }
  ],
  "metadata": {
    "source": "",
    "parsed_at": "",
    "parser_version": "",
    "confidence": 0.0,
    "language": ""
  }
}
}"""
LLM_PROMPT = """You are an information extraction engine.

Your task is to extract structured data from a resume and return VALID JSON ONLY.

STRICT RULES:
- Output must be valid JSON (no markdown, no comments, no explanations)
- Follow the schema EXACTLY
- Use snake_case field names only
- Do NOT invent, infer, or guess any information
- If a field is missing or unclear, use an empty string "" or empty array []
- Dates must be strings (prefer YYYY-MM or YYYY-MM-DD when available)
- Merge bullet points into a single description string
- Do not create array items unless clearly present in the resume
- If uncertain about any value, leave it empty

SCHEMA: {RESUME_SCHEMA}


RESUME TEXT:
{resume_text}
"""
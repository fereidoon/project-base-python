import os
from openai import OpenAI
from prompt import LLM_PROMPT, RESUME_SCHEMA

api_key = os.environ.get('OPENROUTER_API_KEY')
if not api_key:
    raise RuntimeError('OPENROUTER_API_KEY not set in environment')

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)
def call_llm(prompt , model="mistralai/devstral-2512:free"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    test_prompt = "what is the capital of usa"
    print(call_llm(test_prompt))
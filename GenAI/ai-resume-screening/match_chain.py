from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
You are an AI recruiter.

Compare the candidate resume with the job description.

Rules:
- Do NOT assume skills not present
- Only match explicitly mentioned skills
- Be strict and realistic

Resume Data:
{resume_data}

Job Description:
{job_description}

Output:
- Matching Skills
- Missing Skills
- Match Percentage (0–100)

Return in JSON format.
"""
)

match_chain = prompt | llm
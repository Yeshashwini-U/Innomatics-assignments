from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

prompt = PromptTemplate(
    input_variables=["resume_data", "job_description", "score"],
    template="""
You are an AI recruiter explaining your decision.

Given:
- Resume data
- Job description
- Final score

Explain clearly:
- Why this score was assigned
- Strengths of the candidate
- Weaknesses / missing skills

Rules:
- Do NOT assume information
- Be clear and structured

Resume Data:
{resume_data}

Job Description:
{job_description}

Score:
{score}

Output:
- Explanation (clear paragraph or bullet points)
"""
)

explain_chain = prompt | llm
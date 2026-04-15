from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

prompt = PromptTemplate(
    input_variables=["match_result"],
    template="""
You are an AI evaluator.

Based on the matching analysis, assign a score between 0 and 100.

Scoring Guidelines:
- Strong match → 80–100
- Moderate match → 50–79
- Weak match → 0–49

Consider:
- Number of matched skills
- Missing critical skills
- Overall relevance

Match Result:
{match_result}

Output:
- Final Score (0–100)

Return ONLY the score in JSON format:
{{"score": number}}
"""
)

score_chain = prompt | llm
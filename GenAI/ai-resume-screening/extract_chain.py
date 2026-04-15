from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following from the resume:

- Skills
- Tools
- Experience

Return output in JSON format.

Resume:
{resume}
"""
)

extract_chain = prompt | llm
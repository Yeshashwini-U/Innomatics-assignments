from dotenv import load_dotenv
import os

load_dotenv()

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain


def run_pipeline(resume, job_description):

    extracted = extract_chain.invoke({
        "resume": resume
    })

    match = match_chain.invoke({
        "resume_data": extracted.content,
        "job_description": job_description
    })

    score = score_chain.invoke({
        "match_result": match.content
    })

    explanation = explain_chain.invoke({
        "resume_data": resume,
        "job_description": job_description,
        "score": score.content
    })

    return {
        "extracted": extracted.content,
        "match": match.content,
        "score": score.content,
        "explanation": explanation.content
    }


def read_file(path):
    with open(path, "r") as f:
        return f.read()


job_description = read_file("data/job_description.txt")

resumes = {
    "Strong Candidate": read_file("data/strong_resume.txt"),
    "Average Candidate": read_file("data/average_resume.txt"),
    "Weak Candidate": read_file("data/weak_resume.txt")
}


for label, resume in resumes.items():
    print(f"\n\n===== {label} =====\n")

    result = run_pipeline(resume, job_description)

    print("🔹 Extracted Data:\n", result["extracted"])
    print("\n🔹 Match Result:\n", result["match"])
    print("\n🔹 Score:\n", result["score"])
    print("\n🔹 Explanation:\n", result["explanation"])
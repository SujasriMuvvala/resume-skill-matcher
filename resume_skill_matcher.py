import mysql.connector
import argparse
import PyPDF2


def get_resume_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text().lower()
    return text


def get_skills_from_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Muvvala@2007",
        database="resume_skill_matcher"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT name, weight FROM skills")
    skills = dict(cursor.fetchall())
    cursor.close()
    connection.close()
    return skills


def extract_skills(text, skills_db):
    found = set()
    for skill in skills_db:
        if skill in text:
            found.add(skill)
    return found


def weighted_score(matched, required, skills_db):
    total = sum(skills_db[s] for s in required)
    scored = sum(skills_db[s] for s in matched)
    return round((scored / total) * 100, 2) if total else 0


def main():
    parser = argparse.ArgumentParser(description="Resume Skill Matcher using MySQL")
    parser.add_argument("--resume", required=True)
    parser.add_argument("--job", required=True)
    args = parser.parse_args()

    resume_text = get_resume_text(args.resume)

    with open(args.job, "r", encoding="utf-8") as f:
        job_text = f.read().lower()

    skills_db = get_skills_from_db()

    resume_skills = extract_skills(resume_text, skills_db)
    job_skills = extract_skills(job_text, skills_db)

    matched = resume_skills & job_skills
    missing = job_skills - resume_skills
    extra = resume_skills - job_skills

    score = weighted_score(matched, job_skills, skills_db)

    print("\nRESUME SKILL MATCHER REPORT")
    print("-" * 45)
    print(f"Match Score: {score}%")

    print("\nMatched Skills:")
    for s in matched:
        print(f"✔ {s} ({skills_db[s]})")

    print("\nMissing Skills:")
    for s in missing:
        print(f"✘ {s} ({skills_db[s]})")

    print("\nExtra Skills:")
    for s in extra:
        print(f"• {s}")


if __name__ == "__main__":
    main()

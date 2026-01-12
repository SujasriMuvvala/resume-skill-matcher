# Resume Skill Matcher (MySQL)

Resume Skill Matcher is a Python-based command-line application that evaluates
how well a candidate’s resume matches a given job description by comparing
technical skills stored in a MySQL database.

The project focuses on explainable, rule-based matching rather than AI or
machine learning, making the results transparent and easy to interpret.

---

## Features
- Accepts resume PDF and job description text as user input
- Extracts text from resume PDFs using PyPDF2
- Stores technical skills and their importance in a MySQL database
- Performs weighted skill matching using SQL data
- Calculates a percentage-based match score
- Identifies matched, missing, and extra skills

---

## Tech Stack
- Python
- MySQL
- SQL
- PyPDF2
- mysql-connector-python

---

## Database Design
The project uses a MySQL database to store skills in a structured format.

### Table: `skills`
| Column | Description |
|------|------------|
| id | Unique identifier for each skill |
| name | Skill keyword used for matching |
| weight | Importance of the skill for scoring |

Skills are stored as data rather than hardcoded in the application, allowing
easy updates without modifying the code.

---

## Project Structure

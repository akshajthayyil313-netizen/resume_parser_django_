# Resume Parser Django

This is a Django backend project for resume upload and parsing.

## Features
- Upload resumes (PDF, DOC, DOCX)
- Extract name, email, phone, skills
- Handle corrupted and scanned resumes
- Return parsed data as JSON

## Tech Stack
- Python
- Django
- PyPDF2
- python-docx
- pytesseract

## Run Project
pip install -r requirements.txt
python manage.py runserver

## API Endpoints
| Method | Endpoint        | Description                     |
|------|----------------|---------------------------------|
| POST | /api/upload/   | Upload resume and get parsed data |

##Postman Collection
   The exported Postman collection JSON file is included in this repository for API testing.

## Sample API Response
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+91XXXXXXXXXX",
  "skills": ["Python", "Django", "REST API"]
}




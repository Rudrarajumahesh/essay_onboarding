## Essay & Onboarding API (Django)

### Setup
```bash
git clone https://github.com/Rudrarajumahesh/essay_onboarding.git
cd project
python -m venv venv
source venv/bin/activate (for linux)
venv\Scripts\activate (For windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Essay API Requests**

```1. Create Essay
Method: POST
URL: /api/essays/
Headers: Content-Type: application/json

Body:

json

{
  "student_id": "STU123",
  "college_name": "Harvard University",
  "question_title": "Describe a personal challenge you overcame"
}

2. Upload Essay Version (PDF/DOCX)
Method: POST
URL: /api/essays/<essay_id>/versions/
Headers: Content-Type: multipart/form-data

Body (form-data):

Key	Type	Value
content	File	Upload essay file

3. List Essay Versions
Method: GET
URL: /api/essays/<essay_id>/versions/
No body required.

4. Get Latest Essay Version
Method: GET
URL: /api/essays/<essay_id>/latest-version/
No body required.
```


**Student Onboarding API Requests**

```
5. Create Student Profile
Method: POST
URL: /api/student-onboarding/
Headers: Content-Type: application/json

Body:

json

{
  "first_name": "Aarav",
  "last_name": "Sharma",
  "dob": "2007-01-15",
  "gender": "Male",
  "email": "aarav.sharma@example.com",
  "mobile": "+919999888777",
  "address_line": "Flat 101, Green Valley",
  "city": "Hyderabad",
  "zipcode": 500081,
  "state": "Telangana",
  "country": "India",
  "citizenship": "Indian",
  "place_of_birth": "Delhi",
  "current_location": "Hyderabad",
  "guardian_contact": "+918888555111",
  "guardian_relation": "Father",
  "cities_lived": 3,
  "father_profession": "Engineer",
  "mother_profession": "Doctor",
  "family_income": 1200000.00,
  "sibling_name": "Riya Sharma",
  "sibling_age": 14,
  "sibling_institution": "Delhi Public School",
  "abroad_details": "Visited UK for summer school"
}

6. Get Student Profile
Method: GET
URL: /api/student-onboarding/<id>/
No body required.

7. Update Student Profile
Method: PUT
URL: /api/student-onboarding/<id>/
Headers: Content-Type: application/json

Body:

json

{
  "first_name": "Aarav",
  "last_name": "Sharma",
  "city": "Bangalore"
}
```

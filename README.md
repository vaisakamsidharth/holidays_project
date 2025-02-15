# Holidays Project

This project is a full-stack web application that allows users to fetch and display public holidays for different countries. It consists of:

- Backend: Django REST framework (DRF) with an external API integration (Calendarific API)
- Frontend:React.js with tailwind css styling for API requests

# Features
- Fetch holidays from Calendarific API and store them in the database.
- List holidays based on country selection.
- Search holidays by name.
- Caching to optimize API calls.

 Backend Setup (Django + DRF)

1. Install Dependencies**
Ensure you have Python and pip installed, then run:
pip install django djangorestframework django-filter django-cors-headers requests
2. Create & Apply Migrations

python manage.py makemigrations
python manage.py migrate

3. Run the Django Server

python manage.py runserver

Backend will be available at: http://127.0.0.1:8000/api/holidays/

4. API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/holidays/` | GET | Fetch all stored holidays (with filtering & search) |
| `/api/fetch_holidays/<country>/` | GET | Fetch holidays from external API & store in DB |
---------------------------------------------------------------------------------------------------------------
Frontend Setup (React + Tailwind)

Install Dependencies:
Navigate to `holiday_frontend/` and install required packages:
npm install

2. Start the Frontend Server

npm start

Frontend will be available at: http://localhost:3000/

3. Key Files in Frontend**
- components/HolidayList.js`: Fetches & displays holidays (but its not working properly)
- App.js: Main entry point for the app

--------------------------------------------------------------------------------------------------------
Troubleshooting
Frontend Not Displaying Data
- Open browser Console and check for errors.
- Run API manually in browser: `http://127.0.0.1:8000/api/holidays/`
- Ensure Django CORS settings** allow frontend access:
  python settings
  INSTALLED_APPS = ["corsheaders", ...]
  MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware", ...]
  CORS_ALLOW_ALL_ORIGINS = True
  
  Restart Django server if changes were made.

----------------------------------------------------------------------------------------------------------

Project Structure

holidays_project/
│── holidays_app/
│   │── models.py
│   │── views.py
│   │── serializers.py
│   │── urls.py
│── holiday_frontend/
│   │── src/
│   │   │── components/HolidayList.js
│   │   │── App.js
│── manage.py
│── README.md

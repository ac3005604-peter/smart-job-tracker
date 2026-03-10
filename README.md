# Smart Job Tracker

Smart Job Tracker is a backend system designed to help job seekers track job applications and manage interview progress.

使用Py建立後端_為求職者設計的自動化追蹤系統，並使用Git。(已會SpringBoot架構，但當時沒用Git的習慣)

This project demonstrates backend development skills including RESTful API design, database modeling, scheduled tasks, containerization with Docker, and cloud deployment on Google Cloud Platform.

---

## Features

- Create, read, update, and delete job applications
- Track application status (Applied, Interview, Offer, Rejected)
- Store company name, job title, salary range, and notes
- Filter jobs by status
- Salary statistics analysis
- Scheduled reminder for stale applications
- RESTful API documentation via Swagger

---

## Tech Stack

Backend  
- Python  
- FastAPI  

Database  
- PostgreSQL / MySQL  
- SQLAlchemy  

Infrastructure  
- Docker  
- Google Cloud Run  

Scheduler  
- APScheduler

---

## System Architecture

```
Client
  ↓
FastAPI Backend
  ↓
Database (PostgreSQL / MySQL)
  ↓
Scheduler (Reminder System)

Deployment:
Docker → Google Cloud Run
```

---

## API Endpoints

### Job Management

| Method | Endpoint | Description |
|------|------|------|
| POST | /jobs | Create a job application |
| GET | /jobs | Get all job applications |
| GET | /jobs/{id} | Get job application by id |
| PUT | /jobs/{id} | Update job application |
| DELETE | /jobs/{id} | Delete job application |

---

### Filtering

| Method | Endpoint | Description |
|------|------|------|
| GET | /jobs/status/{status} | Get jobs by status |

---

### Salary Statistics

| Method | Endpoint | Description |
|------|------|------|
| GET | /jobs/salary/summary | Get salary statistics |

---

## Example Job Record

```json
{
  "company_name": "ABC Tech",
  "job_title": "Junior Backend Engineer",
  "salary_min": 45000,
  "salary_max": 60000,
  "status": "Applied",
  "applied_date": "2026-03-09",
  "note": "Applied via 104"
}
```

---

## Local Setup

Clone repository

```
git clone https://github.com/yourname/smart-job-tracker.git
cd smart-job-tracker
```

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
uvicorn app.main:app --reload
```

Open browser

```
http://localhost:8000/docs
```

---

## Docker

Build container

```
docker build -t smart-job-tracker .
```

Run container

```
docker run -p 8000:8000 smart-job-tracker
```

---

## Future Improvements

- User authentication
- Email reminder notification
- Frontend dashboard
- Export application data to CSV
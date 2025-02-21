project/
│── backend/
│ │── database/ # Servis za upravljanje bazom podataka
│ │ │── Dockerfile
│ │ │── database.py
│ │
│ │── auth/ # Autentifikacija korisnika
│ │ │── Dockerfile
│ │ │── auth.py
│ │
│ │── crud/ # CRUD operacije nad računima
│ │ │── Dockerfile
│ │ │── crud.py
│ │
│ │── pdf_generator/ # PDF generacija računa
│ │ │── Dockerfile
│ │ │── pdf_generator.py
│ │
│ │── main/ # Glavni FastAPI servis
│ │ │── Dockerfile
│ │ │── main.py
│ │
│ │── models/ # Pydantic modeli (DIJELJENI između servisa)
│ │ │── **init**.py # Za prepoznavanje kao Python modul
│ │ │── models.py # Svi Pydantic modeli
│
│── frontend/ # Flask frontend
│ │── templates/
│ │── static/
│ │── app.py
│ │── Dockerfile
│
│── docker-compose.yml
│── .env

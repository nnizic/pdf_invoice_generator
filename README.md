invoice_app/
│── backend/               # FastAPI backend
│   │── main.py            # Glavna FastAPI aplikacija
│   │── models.py          # Pydantic modeli
│   │── database.py        # Konekcija s DynamoDB
│   │── auth.py            # JWT autentifikacija
│   │── crud.py            # Operacije s računima
│   │── pdf_generator.py   # Generiranje PDF-a
│── frontend/              # Flask frontend
│   │── app.py             # Flask aplikacija
│   │── static/            # CSS datoteke
│   │   │── style.css      # Glavni CSS
│   │── templates/         # HTML predlošci
│   │   │── index.html     # Početna stranica
│   │   │── register.html  # Registracija korisnika
│   │   │── login.html     # Login forma
│   │   │── form.html      # Unos računa
│   │   │── success.html   # Stranica nakon uspješnog unosa
│── docker-compose.yml     # Docker konfiguracija za DynamoDB
│── requirements.txt       # Python paketi

```plaintext
# Struktura projekta

## 📂 invoice_app/

### 📁 backend/ (FastAPI backend)
- 📄 `main.py` - Glavna FastAPI aplikacija
- 📄 `models.py` - Pydantic modeli za validaciju
- 📄 `database.py` - Konekcija s DynamoDB
- 📄 `auth.py` - JWT autentifikacija korisnika
- 📄 `crud.py` - Operacije nad računima (kreiranje, dohvat, brisanje)
- 📄 `pdf_generator.py` - Generiranje PDF-a s računima

### 📁 frontend/ (Flask frontend)
- 📄 `app.py` - Flask aplikacija
- 📁 `static/` - Stilski i statički resursi
  - 🎨 `style.css` - Glavni CSS stilovi
- 📁 `templates/` - HTML predlošci
  - 📄 `index.html` - Početna stranica
  - 📄 `register.html` - Registracija korisnika
  - 📄 `login.html` - Login forma
  - 📄 `form.html` - Forma za unos računa
  - 📄 `success.html` - Stranica nakon uspješnog unosa

### 📄 `docker-compose.yml` - Docker konfiguracija za DynamoDB
### 📄 `requirements.txt` - Python paketi potrebni za aplikaciju
```

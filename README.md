
# Aplicație Django - Rețete Culinare

Această aplicație permite utilizatorilor să creeze, editeze și vizualizeze rețete culinare.

## Funcționalități

- Înregistrare și autentificare utilizatori
- Adăugare, modificare și ștergere rețete (doar pentru autor)
- Afișare rețete pentru toți vizitatorii
- Sortare rețete după titlu sau dată de creare
- Upload imagine pentru rețetă (cu fallback implicit)
- Bootstrap pentru stilizare
- Validare timp de gătire numeric

## Cum rulezi aplicația

1. Clonează proiectul:
   ```bash
   git clone <repo-url>
   cd recipe_project
   ```

2. Instalează dependențele:
   ```bash
   pip install -r requirements.txt
   ```

3. Aplică migrațiile și pornește serverul:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Deschide browserul și accesează:
   ```
   http://127.0.0.1:8000/
   ```

## Pagini disponibile

- `/` – Listă rețete (sortate alfabetic)
- `/data/` – Rețete sortate după dată
- `/recipe/add/` – Adaugă rețetă
- `/recipe/<id>/edit/` – Editează rețetă
- `/recipe/<id>/delete/` – Șterge rețetă
- `/recipe/<id>/` – Detalii rețetă
- `/login/` – Login
- `/logout/` – Logout
- `/register/` – Înregistrare cont

## Testare

Pentru a rula testele:
```bash
python manage.py test recipes
```

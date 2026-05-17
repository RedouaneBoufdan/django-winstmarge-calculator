# Redouane.Boufdan@student.odisee.be 2026-27

# Django Winstmarge Calculator

Dit project is gemaakt voor de opdracht Django 25-26 van Data & Application Integration [OBI36a].

## Doel van het project

Het doel van deze Django-applicatie is om inzicht te krijgen in een Python gebaseerd web framework Django en het MVT-principe toe te passen:

- Model
- View
- Template

De applicatie berekent de winst en de winstmarge op basis van twee ingegeven waarden.

## Context

Deze formule wordt toegepast in een bedrijfseconomische context.

Een gebruiker geeft de aankoopprijs en verkoopprijs in. Daarna berekent de applicatie automatisch de winst en de winstmarge.

## Input

De applicatie gebruikt minstens twee inputvariabelen:

- Aankoopprijs
- Verkoopprijs

## Output

De applicatie toont minstens twee resultaten:

- Winst
- Winstmarge in %

## Formules

Winst = verkoopprijs - aankoopprijs

Winstmarge = winst / verkoopprijs x 100

## Voorbeeld

Input:

- Aankoopprijs: 50
- Verkoopprijs: 80

Output:

- Winst: 30
- Winstmarge: 37.50%

## Django structuur

Het project bestaat uit:

- `business_calculator/` : hoofdproject
- `margin_app/` : Django app
- `margin_app/views.py` : bevat de berekening en de MVT-logica
- `margin_app/models.py` : bevat het Django model
- `margin_app/urls.py` : bevat de URL-routing van de app
- `margin_app/templates/margin_app/calculator.html` : bevat de HTML-template voor de browserweergave
- `manage.py` : Django command-line utility
- `db.sqlite3` : SQLite database

## Development environment

Voor dit project werd een virtuele omgeving gebruikt:

```bash
python -m venv myworld
myworld\Scripts\activate
```

Daarna werd Django geïnstalleerd:

```bash
pip install django
```

## Project starten

Start de development server met:

```bash
python manage.py runserver
```

Open daarna de browser op:

```text
http://127.0.0.1:8000/
```

## GitHub

De opdracht werd gecommit en gepusht naar GitHub zoals gevraagd.

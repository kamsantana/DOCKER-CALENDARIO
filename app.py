from flask import Flask, render_template_string
from datetime import datetime
import calendar

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    year = now.year
    month = now.month
    day_today = now.day

    meses = [
        "", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    nombre_mes = f"{meses[month]} {year}"

    cal = calendar.Calendar(firstweekday=0)
    semanas = cal.monthdayscalendar(year, month)
    
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calendario - Flask</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            body {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #fff;
                padding: 2rem 0;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 2rem;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                max-width: 450px;
                width: 90%;
            }
            h1 {
                font-size: 1.6rem;
                margin-bottom: 1.5rem;
                font-weight: 600;
                letter-spacing: 1px;
            }
            .calendar-grid {
                display: grid;
                grid-template-columns: repeat(7, 1fr);
                gap: 8px;
            }
            .day-name {
                font-weight: bold;
                color: #ff9f1c;
                font-size: 0.85rem;
                padding-bottom: 5px;
                text-transform: uppercase;
            }
            .day {
                padding: 0.6rem 0;
                border-radius: 8px;
                font-size: 0.95rem;
                transition: background 0.3s;
            }
            .day.empty {
                opacity: 0.2;
            }
            .day.today {
                background: #2ec4b6;
                color: #fff;
                font-weight: bold;
                box-shadow: 0 0 10px rgba(46, 196, 182, 0.6);
            }
            .day:not(.empty):not(.today):hover {
                background: rgba(255, 255, 255, 0.15);
                cursor: pointer;
            }
            .footer-info {
                margin-top: 1.5rem;
                font-size: 0.85rem;
                color: #e0e0e0;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📅 {{ nombre_mes }}</h1>
            <div class="calendar-grid">
                <div class="day-name">Lu</div>
                <div class="day-name">Ma</div>
                <div class="day-name">Mi</div>
                <div class="day-name">Ju</div>
                <div class="day-name">Vi</div>
                <div class="day-name">Sá</div>
                <div class="day-name">Do</div>
                
                {% for semana in semanas %}
                    {% for dia in semana %}
                        {% if dia == 0 %}
                            <div class="day empty"></div>
                        {% elif dia == day_today %}
                            <div class="day today">{{ dia }}</div>
                        {% else %}
                            <div class="day">{{ dia }}</div>
                        {% endif %}
                    {% endfor %}
                {% endfor %}
            </div>
            <div class="footer-info">
                Calendario dinámico generado desde Flask 🚀
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(
        html_template, 
        nombre_mes=nombre_mes, 
        semanas=semanas, 
        day_today=day_today
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
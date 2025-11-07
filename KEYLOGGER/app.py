from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT, date TEXT)''')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    skills = [
        {"name": "Python", "level": 90},
        {"name": "Flask", "level": 85},
        {"name": "HTML/CSS", "level": 75},
        {"name": "JavaScript", "level": 60},
        {"name": "SQL", "level": 80}
    ]
    return render_template('about.html', skills=skills)

@app.route('/projects')
def projects():
    projects_list = [
        {
            "title": "Pris Jämförare",
            "description": "Webbscraping app som jämför priser online",
            "technologies": ["Python", "Flask", "BeautifulSoup"],
            "github_url": "https://github.com/you/price-comparer"
        },
        {
            "title": "Todo App",
            "description": "Produktivitet app med användarkonton",
            "technologies": ["Python", "Flask", "SQLite"],
            "github_url": "https://github.com/you/todo-app"
        },
        {
            "title": "Väder Dashboard",
            "description": "Realtids väder data visualisering",
            "technologies": ["Python", "JavaScript", "API"],
            "github_url": "https://github.com/you/weather-dash"
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save to database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages (name, email, message, date) VALUES (?, ?, ?, ?)",
                 (name, email, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        
        flash('Tack för ditt meddelande! Jag återkommer snart.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# API Route
@app.route('/api/projects')
def api_projects():
    projects = [
        {"id": 1, "name": "Webbscraper", "completed": True},
        {"id": 2, "name": "Data Analyzer", "completed": False},
        {"id": 3, "name": "Machine Learning", "completed": False}
    ]
    return {"projects": projects}

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
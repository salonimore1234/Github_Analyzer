from flask import Flask, request, render_template
import requests
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# MySQL Database connection settings (stored in .env)
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com/users/"

# MySQL database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return conn

# Function to get GitHub profile
def get_github_profile(username):
    response = requests.get(GITHUB_API_URL + username)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Save user to database
def save_user_to_db(username, repo_count):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO github_users (username, repo_count) 
    VALUES (%s, %s) 
    ON DUPLICATE KEY UPDATE repo_count = VALUES(repo_count)
    """
    cursor.execute(query, (username, repo_count))
    connection.commit()

    cursor.close()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        profile_data = get_github_profile(username)

        if profile_data:
            # Save the user profile to the database
            save_user_to_db(username, profile_data['public_repos'])

            return render_template('index.html', profile=profile_data)
        else:
            return render_template('index.html', error="User not found!")

    return render_template('index.html')

if __name__ == '_main_':
    app.run(debug=True)
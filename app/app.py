from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['POST'])
def proxy():
    url = request.form.get('url')
    if not url:
        return "No URL provided", 400

    # Ensure the URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        # Forward the request to the URL
        response = requests.get(url)
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, send_from_directory

# Use /static URL path to match vercel.json static route
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download-cv')
def download_cv():
    return send_from_directory('static/files', 'cv.pdf', as_attachment=True)

if __name__ == '__main__':
    # Local development server
    app.run(host='0.0.0.0', port=5000)

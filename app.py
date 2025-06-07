import traceback
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Exception in / route: {e}")
        app.logger.error(traceback.format_exc())
        abort(500)

@app.route('/download-cv')
def download_cv():
    try:
        return send_from_directory('static/files', 'cv.pdf', as_attachment=True)
    except Exception as e:
        app.logger.error(f"Exception in /download-cv route: {e}")
        app.logger.error(traceback.format_exc())
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

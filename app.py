from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # needed for flashing messages

# Home route: renders your portfolio page
@app.route('/')
def home():
    return render_template('index.html')

# Contact form POST handler
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Simple validation (you can expand this)
    if not name or not email or not message:
        flash('Please fill all fields in the contact form.')
        return redirect(url_for('home') + '#contact')

    # Here you could add email sending or saving message to a DB/file
    print(f"New message from {name} ({email}): {message}")

    flash('Thank you for your message! I will get back to you soon.')
    return redirect(url_for('home') + '#contact')

# Serve CV for download
@app.route('/download_cv')
def download_cv():
    # Make sure your CV PDF is saved under /static/files/shashika_cv.pdf
    cv_dir = os.path.join(app.root_path, 'static', 'files')
    return send_from_directory(cv_dir, 'shashika_cv.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, redirect, url_for, render_template
from send_form_data import store_form_data
# from app import app

# @app.route('/')
# def index():
#     return render_template('newForm.html')  # Ensure this matches your HTML file name

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = {
            'full_name': request.form.get('full_name'),
            'job_title': request.form.get('job_title'),
            'department_ai': request.form.get('department'),
            'linkedin_industry': request.form.get('linkedin_industry'),
            'lvl1_industry': request.form.get('lvl1_industry'),
            'lvl2_industry': request.form.get('lvl2_industry'),
            'long_input1': request.form.get('long_input1'),
            'long_input2': request.form.get('long_input2'),
            'long_input3': request.form.get('long_input3'),
            'long_input4': request.form.get('long_input4')
        }
        store_form_data(data)
        return redirect(url_for('success'))
    return render_template('newForm.html')

@app.route('/success')
def success():
    return "Form data submitted successfully!"
from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'templates'))

from models import db, Student
from database import init_db, get_all_students, get_student_by_name, add_student, get_student_by_id, update_student, delete_student_permanently

app = Flask(__name__)
app.secret_key = 'sis_secret_key_2024'

init_db(app)

@app.route('/')
def home():
    total_students = Student.query.filter_by(is_active=True).count()
    return render_template('home.html', total_students=total_students)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_data = {
            'student_name': request.form['student_name'],
            'registration_number': request.form['registration_number'],
            'email': request.form['email'],
            'programme': request.form['programme']
        }
        success, message, student = add_student(student_data)
        if success:
            return render_template('confirmation.html', student=student)
        flash(message, 'error')
    return render_template('register.html')

@app.route('/students')
def students_list():
    students = get_all_students()
    return render_template('student_list.html', students=students)

@app.route('/search')
def search_students():
    query = request.args.get('q', '')
    students = get_student_by_name(query) if query else get_all_students()
    return render_template('student_list.html', students=students, search_term=query)

@app.route('/student/<name>')
def student_profile(name):
    students = get_student_by_name(name)
    student = students[0] if students else None
    return render_template('student_list.html', students=[student] if student else [], search_term=name)

@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = get_student_by_id(student_id)
    if not student:
        flash('Student not found', 'error')
        return redirect(url_for('students_list'))

    if request.method == 'POST':
        update_data = {
            'student_name': request.form['student_name'],
            'registration_number': request.form['registration_number'],
            'email': request.form['email'],
            'programme': request.form['programme']
        }
        success, message = update_student(student_id, update_data)
        if success:
            flash(message, 'success')
            return redirect(url_for('students_list'))
        flash(message, 'error')

    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    student = get_student_by_id(student_id)
    if not student:
        flash('Student not found', 'error')
        return redirect(url_for('students_list'))
    return render_template('delete_confirm.html', student=student)

@app.route('/delete/<int:student_id>/confirm', methods=['POST'])
def confirm_delete_student(student_id):
    success, message = delete_student_permanently(student_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('students_list'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

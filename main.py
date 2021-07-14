from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL settings and connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'izeven_dev'
app.config['MYSQL_PASSWORD'] = 'izeven_pwd'
app.config['MYSQL_DB'] = 'izeven_db'
mysql = MySQL(app)

# Session settings
app.secret_key = "secret key"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET', 'POST'], strict_slashes=False)
def students():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        current_student = request.form['current_student']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO students(student_id, name, last_name, email, current_student) VALUES(%s, %s, %s, %s, %s)", (student_id, name, last_name, email, current_student))
        mysql.connection.commit()
        flash("Student created successfully")
        return redirect(url_for('students'))
    return render_template('students.html')

@app.route('/students/list', methods=['GET'], strict_slashes=False)
def students_list():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM students')
    data = cursor.fetchall()
    return render_template('students_list.html', students = data)

@app.route('/students/list/delete/<string:id>', methods=['GET', 'POST'], strict_slashes=False)
def student_delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM students WHERE student_id = {}'.format(id))
    mysql.connection.commit()
    return redirect(url_for('students_list'))

@app.route('/students/list/edit/<string:id>', methods=['GET', 'POST'], strict_slashes=False)
def student_edit(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM students WHERE student_id = {}'.format(id))
    data = cursor.fetchall()
    return render_template('update_students.html', student = data[0])

@app.route('/students/list/update/<string:id>', methods=['GET', 'POST'], strict_slashes=False)
def student_update(id):
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        current_student = request.form['current_student']
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE students SET name = %s, last_name = %s, email = %s, current_student = %s WHERE student_id = %s', (name, last_name, email, current_student, id))
        mysql.connection.commit()
        return redirect(url_for('students_list'))

@app.route('/courses', methods=['GET', 'POST'], strict_slashes=False)
def courses():
    if request.method == 'POST':
        class_id = request.form['class_id']
        name = request.form['name']
        description = request.form['description']
        cost = request.form['cost']
        duration = request.form['duration']
        remote = request.form['remote']
        on_site = request.form['on_site']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO courses(class_id, name, description, cost, duration, remote, on_site) VALUES(%s, %s, %s, %s, %s, %s, %s)',
        (class_id, name, description, cost, duration, remote, on_site))
        mysql.connection.commit()
        flash("Course created successfully")
        return redirect(url_for('courses'))
    return render_template('courses.html')


@app.route('/classes', methods=['GET', 'POST'], strict_slashes=False)
def classes():
    if request.method == 'POST':
        class_name = request.form['class_name']
        professor = request.form['professor']
        content_hours = request.form['content_hours']
        level = request.form['level']
        available = request.form['available']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO classes(class_name, professor, content_hours, level, available) VALUES(%s, %s, %s, %s, %s)' , (class_name, professor, content_hours, level, available))
        mysql.connection.commit()
        flash("Class created successfully")
        return redirect(url_for('classes'))
    return render_template('classes.html')


@app.route('/grades', methods=['GET', 'POST'], strict_slashes=False)
def grades():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        non_attendance = request.form['non_attendance']
        grade = request.form['grade']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO grades(student_id, course_id, non_attendance, grade) VALUES(%s, %s, %s, %s)', (student_id, course_id, non_attendance, grade))
        mysql.connection.commit()
        flash("Student grade uploaded successfully")
        return redirect(url_for('grades'))
    return render_template('grades.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

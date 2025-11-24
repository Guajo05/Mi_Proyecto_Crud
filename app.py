from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporal para almacenar tareas (en lugar de base de datos)
tasks = []

# Página principal - muestra todas las tareas
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Añadir nueva tarea
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if task_content:
        tasks.append({'id': len(tasks) + 1, 'content': task_content})
    return redirect(url_for('index'))

# Editar tarea - mostrar formulario de edición
@app.route('/edit/<int:task_id>')
def edit_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    return render_template('edit.html', task=task)

# Actualizar tarea - procesar la edición
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task_content = request.form.get('content')
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['content'] = task_content
    return redirect(url_for('index'))

# Eliminar tarea
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
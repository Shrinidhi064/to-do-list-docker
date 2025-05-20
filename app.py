from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route('/')
def index():
    search_query = request.args.get('search', '')

    if search_query:
        tasks = Task.query.filter(Task.content.ilike(f'%{search_query}%')).all()
    else:
        tasks = Task.query.all()

    return render_template('index.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content']
    new_task = Task(content=task_content)
    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your task'

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
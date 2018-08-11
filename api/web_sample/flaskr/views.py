from flask import request, redirect, url_for, render_template, flash
from flask import jsonify
from flaskr import app, db
from flaskr.models import Entry
import random

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新規投稿に成功しました')
    return redirect(url_for('show_entries'))


@app.route('/v1/api/randint')
def random_num():
    response = {
        'randnum': random.randint(0,100)
    }
    return jsonify(response)
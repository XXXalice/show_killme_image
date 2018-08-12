from flask import request, redirect, url_for, render_template, flash
from flask import jsonify
from flaskr import app, db
from flaskr.models import Entry
import random, math, json

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


@app.route('/v1/api/circle/<radius>')
def circle_area(radius):
    try:
        area = math.pi * float(radius) * float(radius)
    except:
        area = "Error."
    response = {
        'area':area
    }
    return jsonify(response)


@app.route('/v1/api/json/<key>', methods=['POST'])
def post(key):
    result = set_property(key, json.loads(request.data))
    return jsonify(result)


def set_property(key, properties):
    file_name = key + '.json'
    data = read_model(file_name)
    if data is None:
        data = {}
    data.update(properties)
    result = write_model(file_name, data)
    return result

def read_model(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return None

def write_model(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=True)
            return data
    except Exception as e:
        print(e)
        return None
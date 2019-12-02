from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sqlite3 as sql
from json import dumps
from flask import render_template
import os

root = os.getcwd()
app = Flask(__name__)
api = Api(app)

conn = sql.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS assets (Aid integer, Name text)')
conn.execute('CREATE TABLE IF NOT EXISTS workers (Wid integer PRIMARY KEY, Firstname text, Lastname text)')
conn.execute('CREATE TABLE IF NOT EXISTS tasks (Tid integer, Task text, Workerid integer NOT NULL, Date text,FOREIGN KEY (Workerid) REFERENCES workers(Wid) )')
conn.commit()
conn.close()

@app.route('/add-assets')
def add_assets():
    return render_template('add_asset.html')

@app.route('/addrec', methods=['POST'])
def addrec():
    if request.method=='POST':
        try:
            id = request.form['object_id']
            name = request.form['oname']

            conn = sql.connect('database.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO assets (Aid, Name) VALUES (?,?)", (id, name))
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            conn.close()

@app.route('/add-task')
def add_task():
    return render_template('add_task.html')

@app.route('/addtrec', methods=['POST'])
def addtrec():
    if request.method=='POST':
        try:
            id = request.form['task_id']
            name = request.form['taname']
            worid = request.form['worid']
            dc = request.form['dc']

            conn = sql.connect('database.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO tasks (Tid, Task, Workerid, Date) VALUES (?,?,?,?)", (id, name, worid, dc))
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            conn.close()


@app.route('/add-worker')
def add_worker():
    return render_template('add_worker.html')

@app.route('/addwrec', methods=['POST'])
def addwrec():
    if request.method=='POST':
        try:
            id = request.form['wid']
            fname = request.form['fname']
            lname = request.form['lname']

            conn = sql.connect('database.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO workers (Wid, Firstname, Lastname) VALUES (?,?,?)", (id, fname, lname))
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            conn.close()

class assets(Resource):
    def get(self):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM assets')
        rows = cur.fetchall()
        conn.close()
        return rows

class task(Resource):
    def get(self, workerid):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM tasks WHERE Workerid = %d' %int(workerid))
        rows = cur.fetchall()
        conn.close()
        return rows



api.add_resource(assets, '/assets/all')
api.add_resource(task, '/get-tasks-for-worker/<workerid>')

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request
import MySQLdb
import utils

app = Flask(__name__)

# Configuration

@app.route('/', methods=['GET', 'POST'])
def mainIndex():
    db = utils.db_connect()
    cur = db.cursor()
    
    # if user typed in a post ...
    if request.method == 'POST':
        query = "INSERT INTO posts VALUES ('" + request.form['name'] + "', '" + request.form['msg'] + "')"
        # Print query to console (useful for debugging)
        print query
        cur.execute(query)
        db.commit()

    cur.execute('select * from posts')
    rows = cur.fetchall()

    return render_template('index.html', posts=rows)

@app.route('/cursor', methods=['GET', 'POST'])
def cursorDictDemo():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    
    # if user typed in a post ...
    if request.method == 'POST':
        query = "INSERT INTO posts VALUES ('" + request.form['name'] + "', '" + request.form['msg'] + "')"
        # Print query to console (useful for debugging)
        print query
        cur.execute(query)
        db.commit()

    cur.execute('select * from posts')
    rows = cur.fetchall()

    return render_template('index2.html', posts=rows)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)

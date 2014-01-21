from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def mainIndex():
    return render_template('index.html')

@app.route('/report')
def report():
  return render_template('report.html')

@app.route('/report2', methods=['POST'])
def report2():
  abduction = {'firstname': request.form['firstname'],
               'lastname': request.form['lastname']}
  return render_template('report2.html', abduction = abduction)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=3000)

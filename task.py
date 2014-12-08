import sqlite3
from bottle import route, run, template

@route('/tasks')
def show_picnic():
    db = sqlite3.connect('development.sqlite3')
    c = db.cursor()
    c.execute("SELECT name FROM tasks limit 20")
    data = c.fetchall()
    c.close()

    all_data = []
    # convert from sqlalchemy to dict
    for row in data:
        data = {}
        for col in row:
            data['name'] = col

        all_data.append(data)

    return {'data':all_data}


    # output = template('bring_to_tasks', rows=data)
    # return output

run(host='0.0.0.0', port=8080)

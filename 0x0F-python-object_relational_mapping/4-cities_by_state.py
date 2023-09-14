#!/usr/bin/python3
"""Reading a database table with join"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) != 4):
        quit()
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = ('SELECT c.id, c.name, s.name FROM cities AS c ' +
             'JOIN states as s ' +
             'WHERE c.state_id = s.id ' +
             'ORDER BY c.id')
    r = cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""Reading a database table with filter"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) != 5):
        quit()
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = 'SELECT * FROM states ' + 'WHERE name = \'{}\''.format(sys.argv[4])
    if (query.count('states') == 1):
        r = cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""Reading a database table with join"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) != 5):
        quit()
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = ('SELECT c_name FROM ' +
             '(SELECT c.id, c.name as c_name, ' +
             's.name as s_name FROM cities AS c ' +
             'JOIN states as s ' +
             'WHERE c.state_id = s.id ' +
             'ORDER BY c.id) j ' +
             'WHERE LOWER(j.s_name) = LOWER(\'{}\')'.
             format(sys.argv[4]))
    if (query.count('states') == 1 and query.count('cities') == 1):
        r = cur.execute(query)
        rows = cur.fetchall()
        res = ''
        for row in rows:
            for col in row:
                res += col
                res += ', '
        print(res[0:-2])

    cur.close()
    db.close()

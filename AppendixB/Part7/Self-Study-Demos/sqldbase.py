# Database script to populate and query an SQLite database, stored in people.db

import sqlite3, time
conn = sqlite3.connect('people.db')    # Filename for database storage
curs = conn.cursor()                   # Submit SQL through cursor

# Make+fill table if doesn't yet exist
tbl = curs.execute('select name from sqlite_master where name = \'people\'')
if tbl.fetchone() is None:
    print('Making table anew')
    curs.execute('create table people (name, job, pay)')

    recs = [('Pat', 'mgr', 40000), ('Sue', 'dev', 60000), ('Bob', 'dev', 50000)]
    for rec in recs:
        curs.execute('insert into people values (?, ?, ?)', rec)
    conn.commit()

# Show all rows
print('Rows:')
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)

# Show just devs
print('Devs:')
curs.execute("select name, pay from people where job = 'dev'")
colnames = [desc[0] for desc in curs.description]
while row := curs.fetchone():
    print('-' * 30)
    for (name, value) in zip(colnames, row):
        print(f'{name:<4} => {value}')

# Update devs' pay: shown on next run
secs = int(time.time())  # UTC!
curs.execute('update people set pay = ? where job = ?', [secs, 'dev'])
conn.commit()


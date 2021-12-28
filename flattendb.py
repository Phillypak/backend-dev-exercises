############################################
# code for flattening exercise01.sqlite database
# Saved to database.db
# flattened import to CSV
############################################
import sqlite3 as sql
ex01 = sql.connect("exercise01.sqlite")
db = sql.Connection('database.db')

cursor = ex01.cursor()
dbcursor = db.cursor()

# Resets databse every run
dbcursor.execute("DELETE FROM Records")

# create a new table
dbcursor.execute("""CREATE TABLE IF NOT EXISTS Records(
                        id INTEGER, age INTEGER, workclass TEXT, education_level TEXT, 
                        education_num TEXT, marital_status TEXT, occupation TEXT, relationship TEXT,
                        race TEXT, sex TEXT, capital_gain INTEGER, capital_loss INTEGER, hours_week INTEGER, 
                        country TEXT, over_50k BOOLEAN)""")
db.commit()

# select all items and insert them into the new databse
for item in cursor.execute("""SELECT r.id, r.age, w.name, e.name, m.name, o.name, rs.name, 
                                rc.name, s.name, r.capital_gain, r.capital_loss, r.hours_week, c.name, r.over_50k
                                FROM records r, workclasses w, education_levels e, 
                                    marital_statuses m, occupations o, races rc, relationships rs, 
                                    sexes s, countries c
                                where w.id=r.workclass_id
                                    AND e.id=r.education_level_id
                                    AND m.id=r.marital_status_id
                                    AND o.id=r.occupation_id
                                    AND rc.id=r.race_id
                                    AND rs.id=r.relationship_id
                                    AND s.id=r.sex_id
                                    AND c.id=r.country_id""").fetchall():
    exec = "INSERT INTO Records(id, age, workclass, education_level, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_week, country, over_50k) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    execdata = (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13])
    dbcursor.execute(exec, execdata)

# commit changes
db.commit()

#print(dbcursor.execute("select * from Records limit 1").fetchall())

###############################
# ISSUES due to time constraint:
# Does not import education_num
# Slightly long run time
###############################
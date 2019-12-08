from sqlalchemy import *
import sqlalchemy as db

# konekcija
engine = db.create_engine('oracle+cx_oracle://stevan:test@localhost:1521/XE', max_identifier_length=128)

connection = engine.connect()

# Kako napraviti tabelu kroz Python? Jedan od nacina je preko query-ja koji bi koristili u SQL Developeru
# CREATE, INSERT

with connection as con:
    '''
    con.execute('CREATE TABLE projekat (broj NUMBER(38, 0) NOT NULL, opis VARCHAR(50), id NUMBER(38, 0) NOT NULL, '
                'PRIMARY KEY (broj), FOREIGN KEY (id) REFERENCES korisnici(id))')
    
    con.execute("INSERT INTO projekat (broj, opis, id) VALUES (1, 'predstaviti Pandas', 3)")
    con.execute("INSERT INTO projekat (broj, opis, id) VALUES (2, 'predstaviti Binary Tree', 1)")
    con.execute("INSERT INTO projekat (broj, opis, id) VALUES (3, 'predstaviti LinkedLists', 3)")
    con.execute("INSERT INTO projekat (broj, opis, id) VALUES (4, 'predstaviti SQLalchemy', 6)")
    
    # kod sa linije ispod se nece izvrsiti, zasto?
    con.execute("INSERT INTO projekat (broj, opis, id) VALUES (1, 'predstaviti Pandas', 20)")
    '''

    projects = con.execute('SELECT * FROM projekat')
    for row in projects:
        print(row)

    # Hocemo da dobijemo opis projekta za odredjenu osobu
    one_project = con.execute("SELECT opis FROM projekat WHERE id  = (SELECT id FROM korisnici WHERE ime = 'Caka')")
    for row in one_project:
        # rezultat vraca torku sa samo jednim elementom, pa uzimamo taj prvi element iz nje
        print("Opis projekta za korisnika Caka je: ", row[0])

# Drugi nacin za kreiranje tabele
# Nece raditi jer tabela korisnici nije kreirana na ovaj nacin
'''
metadata = MetaData()
new_table = Table('partner', metadata,
                  Column('partner_id', Integer, primary_key=True),
                  Column('id_korisnika', NUMERIC(38, 0), ForeignKey('korisnici.id'), nullable=False),
                  Column('ocena', NUMERIC(9, 0)),
                  Column('ime', VARCHAR(20)))
metadata.create_all(engine)

ins = new_table.insert().values(partner_id=1, id_korisnika=5, ocena=9, ime='Petra')
conn = engine.connect()
result = conn.execute(ins)
'''
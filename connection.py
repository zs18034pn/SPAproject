import sqlalchemy as db # importovanje paketa
engine = db.create_engine('oracle+cx_oracle://stevan:test@localhost:1521/XE', max_identifier_length=128)

# metoda connect() konektuje engine koja sadrzi connection string na bazu
connection = engine.connect()

# koristimo metodu table_names() koji vraca imena tabela iz baze; na pocetku nije vracao nista
print(engine.table_names())

# Tabela korisnici je napravljena kroz SQL Developer, a sad ubacujemo podatke kroz Python
# Koristimo metod execute() koji izvršava query koji je u obliku stringa

with connection as con:
    '''
    con.execute("INSERT INTO Korisnici (id, ime, prezime) values (4, 'Milica', 'Milanovic')")
    con.execute("INSERT INTO Korisnici (id, ime, prezime) values (5, 'Petar', 'Petrovic')")
    con.execute("INSERT INTO Korisnici (id, ime, prezime) values (7, 'Ksenija', 'Jovovic')")
    '''
    rs = con.execute('SELECT * FROM Korisnici')
    users = con.execute('SELECT id, ime FROM Korisnici ORDER BY id')

    print("Svi korisnici: ")
    for row in rs:
        print(row)

    print("Korisnici poređani po id-u: ")
    for row in users:
        print(row)

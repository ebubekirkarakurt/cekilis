import sqlite3 as sql 

def main():
    try:
        db = sql.Connection("Cekilis.db")
        cursor = db.cursor()
        sorgu = """CREATE TABLE IF NOT EXISTS Basvuranlar 
        (isim TEXT, soyisim TEXT, numara TEXT, 
        sehityakini TEXT, emekli TEXT, engeldurumu TEXT, ozeldurumyok TEXT)"""

        cursor.execute(sorgu)
        print("Tablo olusturulmustur.")

    except:
        print("Tablo Olsuturulma Hatasi!")

    finally:
        db.close()

if __name__ == "__main__":
    main()
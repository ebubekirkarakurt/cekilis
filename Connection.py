import sqlite3 as sql 

def main():
    try:
        db = sql.Connection("Cekilis.db")
        print("Veritabani olsuturulmustur.")
    except:
        print("Veritabanı Olsuturulma Hatası")
    finally:
        db.close()

if __name__ == "__main__":
    main()
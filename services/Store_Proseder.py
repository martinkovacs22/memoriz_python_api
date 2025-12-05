# Store_Procedure.py

import os
from dotenv import load_dotenv
import mysql.connector
from pydantic import BaseModel

# .env betöltése
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME")  # a .env-ben legyen DB_NAME=adatbazis_nev

def call_stored_procedure(sp_name: str, params: BaseModel):
    """
    Meghív egy tárolt eljárást a paraméterként adott BaseModel alapján.
    
    sp_name: str -> a tárolt eljárás neve
    params: BaseModel -> a BaseModel objektum, amelynek mezői a SP paraméterei lesznek
    """
    # Kapcsolódás az adatbázishoz
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    try:
        cursor = conn.cursor(dictionary=True)

        # BaseModel mezőinek lekérése dict-ként
        param_dict = params.dict()
        # Csak az értékeket vesszük, sorrendben, ahogy a SP várja
        param_values = list(param_dict.values())

        # Tárolt eljárás hívása
        cursor.callproc(sp_name, param_values)

        # Eredmények összegyűjtése (ha van SELECT a SP-ben)
        results = []
        for result in cursor.stored_results():
            results.append(result.fetchall())

        conn.commit()
        return results

    finally:
        cursor.close()
        conn.close()

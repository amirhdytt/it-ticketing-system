from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app) # Mengizinkan Front-End mengakses API ini

# Konfigurasi koneksi ke database MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',      # Sesuaikan jika user MySQL Anda berbeda
    'password': '',      # Kosongkan jika menggunakan XAMPP default
    'database': 'it_support_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# 1. Endpoint POST: Menerima data laporan dari Front-End dan menyimpannya ke Database
@app.route('/api/tickets', methods=['POST'])
def tambah_tiket():
    try:
        data = request.json
        nama = data['nama_pelapor']
        kendala = data['kendala']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Query SQL untuk memasukkan data
        sql_query = "INSERT INTO tickets (nama_pelapor, kendala) VALUES (%s, %s)"
        cursor.execute(sql_query, (nama, kendala))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return jsonify({"pesan": "Laporan kendala berhasil dikirim!"}), 201

    except Exception as e:
        # Dokumentasi error untuk proses debugging
        return jsonify({"error": str(e)}), 500

# 2. Endpoint GET: Mengirimkan data dari Database ke Front-End (Dashboard)
@app.route('/api/tickets', methods=['GET'])
def ambil_semua_tiket():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # dictionary=True agar output berupa JSON object
        
        # Query SQL untuk mengambil data
        cursor.execute("SELECT * FROM tickets ORDER BY tanggal DESC")
        tickets = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return jsonify(tickets), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Menjalankan server Back-End di port 5000
    app.run(debug=True, port=5000)
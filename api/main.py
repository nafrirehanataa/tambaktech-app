from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from datetime import datetime
import asyncio # Menambahkan modul untuk efek delay/loading

app = FastAPI(title="TambakTech Enterprise Core Backend", version="10.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

class LoginData(BaseModel):
    username: str
    password: str

# 1. API Endpoint Login
@app.post("/api/login")
async def process_login(data: LoginData):
    if data.username == "nafrirehanata" and data.password == "tambaktech2026":
        return {"message": "Autentikasi Berhasil", "token": "tambak_secure_jwt_token"}
    raise HTTPException(status_code=401, detail="Kredensial tidak terdaftar di Database")

# 2. API Endpoint TambakBot (Kamus Lengkap & Efek Loading Dikembalikan)
@app.post("/api/chat")
async def ask_tambak_bot(data: ChatMessage):
    msg = data.message.lower()
    
    # MENGEMBALIKAN EFEK LOADING: Jeda 1.8 detik agar animasi "typing..." muncul di web
    await asyncio.sleep(1.8)
    
    # Kamus NLP lengkap persis seperti sebelum eksperimen Gemini
    if "kualitas air" in msg or "kondisi" in msg or "analisis" in msg:
        reply = "Berdasarkan pemindaian sensor terbaru di <b>Kolam Alpha</b>:<br><br><ul style='padding-left:20px;'><li style='margin-bottom:8px'><b>Dissolved Oxygen (DO):</b> Terbaca <b>5.5 mg/L</b>. Memenuhi standar batas aman 3.0 mg/L.</li><li style='margin-bottom:8px'><b>Derajat Keasaman (pH):</b> 7.8 (Kondisi basa lemah, ideal).</li><li style='margin-bottom:8px'><b>Suhu Air:</b> Stabil pada rentang biologis.</li></ul><b>Kesimpulan:</b> Tidak ditemukan parameter berbahaya di Kolam Alpha."
    elif "pakan" in msg or "makan" in msg or "rekomendasi" in msg:
        reply = "Untuk Kolam Alpha:<br><br>Mengingat suhu air saat ini berada pada kurva puncaknya, laju metabolisme usus udang sangat cepat.<br><br><b>Rekomendasi Feeding Program (F/R):</b><br>Berikan <b>32 Kg</b> pakan hari ini dengan rasio 30% Pagi, 40% Siang, dan 30% Malam untuk meminimalisir penumpukan limbah organik di dasar tambak."
    elif "fcr" in msg or "jelaskan" in msg:
        reply = "Secara terminologi ilmu Akuakultur, <b>Feed Conversion Ratio (FCR)</b> adalah indikator efisiensi budidaya.<br><br><i>FCR = Total Berat Pakan yang Disebar ÷ Total Bobot Udang yang Dipanen</i>.<br><br><div style='background:#f0f4f8; padding:10px; border-radius:10px; margin-top:10px;'><b>Analogi:</b> Jika Anda menebar 1500 Kg pakan dan sukses memanen 1000 Kg udang, nilai FCR Anda adalah <b>1.5</b>. Semakin kecil angkanya, margin keuntungan Anda semakin tebal.</div><br>TambakTech mencegah udang stres (DO drop), sehingga nafsu makan stabil dan FCR tertekan menjadi sangat rendah."
    elif "penyakit" in msg or "cegah" in msg or "mati" in msg:
        reply = "<b>Protokol Pencegahan Penyakit TambakTech:</b><br><br>Kematian masal akibat WSSV atau AHPND sangat dihindari. Tindakan preventifnya adalah:<br><br>1. Jaga fluktuasi pH pagi-sore agar tidak lebih dari 0.5 skala.<br>2. Pastikan Oksigen (DO) malam hari selalu berada di atas 4.0 mg/L.<br>3. Suplementasi imunostimulan (Vitamin C) pada pakan.<br><br>Saat ini, parameter air (WQI) di Kolam Alpha terpantau <b>aman dari stresor lingkungan</b>."
    elif "siapa kamu" in msg or "gemini" in msg or "bot" in msg:
        reply = "Saya adalah <b>TambakBot</b>, asisten <i>Artificial Intelligence</i> yang terintegrasi secara bawaan pada ekosistem cloud TambakTech.<br><br>Saya memiliki kapabilitas tinggi dalam memproses data IoT Anda secara real-time dan memberikan wawasan prediktif (forecasting) terkait kualitas air dan manajemen teknis tambak udang Anda."
    elif "terima kasih" in msg or "makasih" in msg or "oke" in msg:
        reply = "Dengan senang hati, Bapak Nafri! Prioritas utama algoritma saya adalah memastikan keamanan aset biologis tambak Anda dan memicu keberhasilan panen yang maksimal. Jangan ragu memanggil saya jika Anda membutuhkan analisis data lanjutan. 🦐📈"
    elif "bantuan" in msg or "tolong" in msg or "menu" in msg:
        reply = "Saya siap menjadi kopilot operasional Anda! Anda dapat meminta analisis spesifik dengan mengetik instruksi berikut:<br><br><ul style='padding-left:20px;'><li>📊 <b>Kondisi Air:</b> \"Tolong analisis kualitas air Kolam Beta\"</li><li>🍤 <b>Pakan:</b> \"Berapa rekomendasi porsi pakan yang ideal?\"</li><li>⚠️ <b>Penyakit:</b> \"Bagaimana strategi mencegah penyakit udang?\"</li><li>📉 <b>Teori:</b> \"Tolong jelaskan secara rinci tentang FCR\"</li></ul>"
    elif "cuaca" in msg or "hujan" in msg or "panas" in msg:
        reply = "Sistem telah terhubung dengan API satelit pemantauan cuaca BMKG. Berdasarkan koordinat operasi Anda, iklim saat ini di area tambak terpantau <b>Sesuai dengan widget Beranda Anda</b>.<br><br>Selalu pastikan kincir air (aerator) beroperasi penuh saat cuaca terik untuk memecah stratifikasi suhu dan mencegah defisit oksigen terlarut di dasar kolam."
    elif "halo" in msg or "hai" in msg or "pagi" in msg or "siang" in msg:
        reply = "Selamat datang, Pak Nafri! Subsistem NLP saya telah teraktivasi.<br><br>Saya memantau indikator komprehensif tambak Anda mencetak skor <b>WQI yang sangat baik</b> hari ini. Ada variabel spesifik yang ingin kita bedah secara statistik?"
    else:
        reply = "Mohon maaf, frasa tersebut belum terpetakan dalam matriks <i>Natural Language Processing</i> (NLP) saya.<br><br>Silakan formulasikan ulang menggunakan kata kunci spesifik operasional tambak seperti: <b>Oksigen, Pakan, Penyakit, Cuaca, Kolam Alpha, atau FCR.</b>"
        
    return {"reply": reply}

# 3. API Endpoint Sensor & Prediksi
@app.get("/api/sensor-data")
async def fetch_sensor_data(pond_id: str = "Alpha"):
    base_do = 5.5 if pond_id == "Alpha" else 4.2
    return {
        "pond": pond_id,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "sensor_readings": {
            "dissolved_oxygen": round(base_do + random.uniform(-0.2, 0.5), 2),
            "temperature": round(28.5 + random.uniform(-0.5, 1.0), 1),
            "ph_level": round(7.8 + random.uniform(-0.1, 0.2), 1)
        }
    }

@app.get("/api/predict")
async def fetch_prediction():
    future_labels = []
    predicted = []
    for i in range(1, 6):
        future_labels.append(datetime.now().timestamp() + (i*60))
        predicted.append(round(5.5 - (i * 0.1) + random.uniform(-0.2, 0.2), 2))
        
    return {
        "future_timestamps": future_labels,
        "predicted_do": predicted,
        "warning_triggered": True if predicted[-1] < 3.0 else False
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
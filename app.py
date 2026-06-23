import streamlit as st

# Ini bagian "Tools + Memory" 
DATABASE_KAMPUS = {
    "ukt": "Info UKT STIKOM Yos Sudarso 2026 cek di SIAKAD atau hubungi BAU.",
    "siakad": "SIAKAD: https://siakad.stikomyos.ac.id. Login pake NIM untuk cek KHS, KRS, jadwal.",
    "bootcamp": "Tugas Bootcamp AI Agent 19 Juni 2026 dikumpul maksimal 23 Juni 2026 jam 23:59 WIB format PDF.",
    "jadwal": "Jadwal kuliah & dosen ada di SIAKAD menu Jadwal Kuliah.",
    "alamat": "STIKOM Yos Sudarso: Jl. SMP 5 Karang Klesem, Purwokerto Selatan."
}

# DEPLOY: Web App Streamlit
st.set_page_config(page_title="AI Agent STIKOM", page_icon="🤖")
st.title("AI Agent STIKOM Yos Sudarso - Bootcamp 19 Juni 2026")
st.write("AI Agent dengan arsitektur Perceive-Reason-Act-Observe")

# 1. PERCEIVE: Tangkap input user
user_input = st.text_input("Perceive: Ketik pertanyaan kamu")

if user_input:
    # 2. REASON: Analisis + Planning
    pertanyaan = user_input.lower()
    hasil = "Pertanyaan belum ada di database. Coba tanya: UKT, SIAKAD, bootcamp, jadwal, atau alamat."
    
    for keyword, jawaban in DATABASE_KAMPUS.items():
        if keyword in pertanyaan:
            hasil = jawaban
            break
    
    # 3. ACT + 4. OBSERVE: Kasih output
    st.text_area("Act: Jawaban AI Agent", value=hasil, height=100)
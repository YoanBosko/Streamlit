import streamlit as st
from responseprocessing import *

def index():
    st.title("SG AI Week 14")
    st.text("Ini adalah teks")
    st.header("Tutorial Streamlit")
    nama = st.text_input(label="Nama", value="masukkan nama anda disini", key="input")
    nim = st.text_input("NIM", key="input2")

    if nama:
        st.text("Nama: " + nama)
        if len(nim) == 10:
            st.text("NIM: " + nim)

    box = st.selectbox("pilih jurusan: ", ["RPL", "IF", "DS", "IT"])
    st.write("pilihan anda adalah \n" + box)
    st.text("pilihan anda adalah \n " + box)

    umur = st.slider("Umur", 1 , 70 , 100)
    st.write(umur)

    gender = st.radio("Gender", ["Pria", "Wanita"])
    if gender == "Pria":
        st.write(f"Hello Mr.{nama}")
    else:
        st.write(f"Hello Mrs.{nama}")

    list_hobi = st.text_area("Hobi", "Main bola, main game")
    list_hobi = [x.strip() for x in list_hobi.split(',')]

    st.write(list_hobi)

    st.divider()
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9IUsEJnumAe1mtHR9xldEGRYtz7DsyS2Tug&s", caption="kucing", width=200)

    st.markdown(
        "[ini link ke google](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9IUsEJnumAe1mtHR9xldEGRYtz7DsyS2Tug&s)"
    )

    st.markdown("# Header")
    st.header("Header")
    st.markdown("## Header")
    st.markdown("###### Header")

    import pandas as pd

    data = {
        'pekerjaan': ['Programmer', 'Dokter', 'Pengacara'],
        'Tier' : ["E", "SS", "A"]
    }

    df = pd.DataFrame(data)
    st.dataframe(data=df, use_container_width=True)

    st.title("Buka Data")
    file = st.file_uploader("Pilih file", type=['jpg', 'csv'])

    if file is not None:
        st.write(file.type)

        if file.type == "image/jpeg":
            st.image(file)
        else:
            data = pd.read_csv(file)
            st.dataframe(data)

    st.divider()

    num1 = st.number_input("Masukkan angka pertama", value=0)
    num2 = st.number_input("Masukkan angka kedua", value=0)

    operasi = st.radio("Pilihan operasi", ["Penjumlahan", "Pengurangan", "Perkalian","Pembagian"])

    if st.button('hitung'):
        if operasi == "Penjumlahan":
            hasil = num1 + num2
        elif operasi == "Pengurangan":
            hasil = num1 - num2

        st.success(f'Hasil {operasi} : {hasil}')

st.sidebar.title("Menu")
st.sidebar.header("Profile")
if st.sidebar.checkbox("Biodata"):
    st.sidebar.text(f"nama: {nama} \nNIM: {nim}")

def direct_chat(text, role):
    with st.chat_message(role):
        st.write(text)

def chatbot():
    st.header("Tampilan chatbot")
    prompt = st.chat_input("ketik sesuatu")
    if prompt:
        direct_chat(prompt, role="user")
        response = generate_response(prompt)
        direct_chat(response, role="assistant")

    
choice = st.sidebar.radio(label="Pilihan", options=["index", "chatbot"])
if choice == "index":
    index()
else:
    chatbot()
import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

Vehicle_type = st.number_input('Input Jenis Kendaraan (0 = Passenger / 1 = Car)') 
Engine_size = st.number_input('Input Ukuran Mesin Mobil (liter)')
Horsepower = st.number_input('Input Tenaga Mobil (Horsepower)')
Curb_weight = st.number_input('Input Berat Kendaraan (Pounds)')
Fuel_capacity = st.number_input('Input Kapasitas Bahan Bakar Mobil (gallon AS)')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[Vehicle_type, Engine_size, Horsepower, Curb_weight, Fuel_capacity]]
    )
    st.write('Estimasi harga mobil dalam Dollar US : ', predict)
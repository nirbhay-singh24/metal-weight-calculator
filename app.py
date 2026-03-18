import streamlit as st
import math

st.set_page_config(page_title="Metal Weight Calculator", layout="centered")

st.title("Metal Weight Calculator")

#Material Densities (kg/m^3)
materials = {
    "Steel": 7850,
    "Aluminium": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Bronze": 8880,
    "Iron": 7860,
    "SS 304/310": 7920,
    "SS 316/321": 7940,
    "SS 410/430": 7710
}

shape = st.selectbox("Select Shape" , ["Round Bar", "Round Tube", "Sheet", "Hexagon", "Square Bar", "Square Tube", "T Bar", "Beam", "Channel", "Angle", "Flat Bar"])
material = st.selectbox("Select Material", list(materials.keys()))

density = materials[material]

st.subheader("Enter Dimensions (in mm)")

if shape == "Sheet":
    L = st.number_input("Length")
    B = st.number_input("Width")
    T = st.number_input("Thickness")

    volume = (L/1000)*(B/1000)*(T/1000)

elif shape == "Round Bar":
    D = st.number_input("Diameter")
    L = st.number_input("Length")
    
    volume = math.pi * (D/2000)**2 * (L/1000)

elif shape == "Round Tube":
    OD = st.number_input("Outer Diameter")
    ID = st.number_input("Inner Diameter")
    L = st.number_input("Length")

    volume = math.pi * ((OD/2000)**2 -(ID/2000)**2) * (L/1000)

elif shape == "Hexagon":
    

if st.button("Calculate"):
    weight = volume * density
    st.success(f"Weight = {weight:.2f} kg")

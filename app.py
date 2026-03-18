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

shape = st.selectbox("Select Shape" , ["Round Bar", "Round Tube", "Sheet", "Hexagon", "Square Bar", "Square Tube", "Flat Bar"])
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
    A = st.number_input("Side")
    L = st.number_input("Length")

    volume = ((3**(1/2) * A**2)/2) * L

elif shape == "Square Bar":
    A = st.number_input("Side")
    L = st.number_input("Length")

    volume = A**2 * L

elif shape == "Square Tube":
    A = st.number_input("Side 1")
    B = st.number_input("Side 2")
    T = st.number_input("Thickness")
    L = st.number_input("Length")

    volume = L * (A * B - (A - 2 * T) * (B - 2 * T))

elif shape == "Flat Bar":
    A = st.number_input("Side 1")
    B = st.number_input("Side 2")
    L = st.number_input("Length")

    volume = L * A * B


if st.button("Calculate"):
    weight = volume * density
    st.success(f"Weight = {weight:.2f} kg")

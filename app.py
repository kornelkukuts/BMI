import streamlit as st

# Oldal konfiguráció
st.set_page_config(page_title="BMI Kalkulátor", page_icon="⚖️", layout="centered")

st.title("⚖️ Testtömegindex (BMI) Kalkulátor")
st.markdown("Számítsd ki a testtömegindexedet és tudd meg az egészségügyi kategóriádat.")

# Beviteli mezők
col1, col2 = st.columns(2)

with col1:
    height_str = st.text_input("Testmagasság (cm):", "175")
with col2:
    weight_str = st.text_input("Testtömeg (kg):", "70")

# Kategória meghatározó függvény
def get_bmi_category(bmi):
    if bmi < 16.0:
        return "Súlyos soványság", "red"
    elif 16.0 <= bmi < 18.5:
        return "Soványság", "orange"
    elif 18.5 <= bmi < 25.0:
        return "Normális / Optimális testsúly", "green"
    elif 25.0 <= bmi < 30.0:
        return "Túlsúly", "orange"
    elif 30.0 <= bmi < 35.0:
        return "I. fokú elhízás", "red"
    elif 35.0 <= bmi < 40.0:
        return "II. fokú elhízás", "red"
    else:
        return "III. fokú (kóros) elhízás", "red"

# Számítás gomb
if st.button("BMI Kiszámítása", type="primary"):
    try:
        height_clean = height_str.strip().replace(",", ".")
        weight_clean = weight_str.strip().replace(",", ".")
        
        height_cm = float(height_clean)
        weight_kg = float(weight_clean)

        if height_cm <= 0 or weight_kg <= 0:
            st.error("Kérjük, pozitív számokat adj meg!")
        else:
            height_m = height_cm / 100.0
            bmi = weight_kg / (height_m ** 2)

            category, status_type = get_bmi_category(bmi)

            # Eredmény megjelenítése stílusosan
            st.success(f"**Számított BMI:** {bmi:.1f}")
            
            if status_type == "green":
                st.info(f"**Kategória:** {category}")
            elif status_type == "orange":
                st.warning(f"**Kategória:** {category}")
            else:
                st.error(f"**Kategória:** {category}")

    except ValueError:
        st.error("Kérjük, érvényes számokat adj meg a magasságnál és a súlynál!")

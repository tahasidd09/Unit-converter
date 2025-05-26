import streamlit as st

# Design-o-Pedia Header
st.markdown("""
    <style>
        .header-container {
            display: flex;
            align-items: center;
        }
        .header-container img {
            width: 50px; /* Adjust logo size */
            margin-right: 10px;
        }
        .header-text {
            font-size: 24px;
            color: blue;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit Columns for Logo and Text
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo1.png", width=50)  # Ensure file name matches

with col2:
    st.markdown("<span class='header-text'>Design-o-Pedia Unit Converter</span>", unsafe_allow_html=True)

# Header with Logo
# st.markdown("<div class='header-container'><img src='logo.png'><span class='header-text'>Design-o-Pedia Unit Converter</span></div>", unsafe_allow_html=True)


# Conversion Functions
def length_converter(length, unit):
    conversion_rates = {
        "Kilometer": length / 1000,
        "Feet": length * 3.28084
    }
    return conversion_rates.get(unit, None)

def temperature_converter(temp_celsius):
    return (temp_celsius * 9/5) + 32

def time_converter(time, unit):
    conversion_rates = {
        "Seconds": time,
        "Minutes": time / 60,
        "Hours": time / 3600
    }
    return conversion_rates.get(unit, None)

def weight_converter(weight, unit):
    conversion_rates = {
        "Grams": weight * 1000,
        "Kilograms": weight,
        "Pounds": weight * 2.20462
    }
    return conversion_rates.get(unit, None)



# Streamlit App
st.title("Unit Converter")

# Conversion Type Selection
choice = st.radio("Select Conversion Type:", ["Length", "Temperature", "Time", "Weight"])

# Length Conversion
if choice == "Length":
    length = st.number_input("Enter length in meters:", min_value=0.0, step=0.1)
    unit = st.selectbox("Convert to:", ["Kilometer", "Feet"])
    
    if st.button("Convert Length"):
        result = length_converter(length, unit)
        st.success(f"Converted Value: {result} {unit}")

# Temperature Conversion
elif choice == "Temperature":
    temp_celsius = st.number_input("Enter temperature in Celsius:", step=0.1)
    
    if st.button("Convert Temperature"):
        result = temperature_converter(temp_celsius)
        st.success(f"Converted Value: {result} Fahrenheit")

# Time Conversion
elif choice == "Time":
    time = st.number_input("Enter time in seconds:", min_value=0.0, step=1.0)
    unit = st.selectbox("Convert to:", ["Seconds", "Minutes", "Hours"])
    
    if st.button("Convert Time"):
        result = time_converter(time, unit)
        st.success(f"Converted Value: {result} {unit}")

# Weight Conversion
elif choice == "Weight":
    weight = st.number_input("Enter weight in kilograms:", min_value=0.0, step=0.1)
    unit = st.selectbox("Convert to:", ["Grams", "Kilograms", "Pounds"])
    
    if st.button("Convert Weight"):
        result = weight_converter(weight, unit)
        st.success(f"Converted Value: {result} {unit}")

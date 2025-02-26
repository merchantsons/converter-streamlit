import streamlit as st
import math
import random

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Unit Converter By Merchantsons",
        page_icon="🔄",
        layout="centered"
    )
    
    # Apply custom CSS for better styling including the gradient background
    apply_custom_css()
    
    # Create container for main content
    main_container = st.container()
    
    with main_container:
        # Logo and title in a colorful header
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("# 🔄")
        with col2:
            st.markdown("<h1 style='font-size: 1.8rem; margin-bottom: 0px; color: #000;'>GOOGLE LIKE UNIT CONVERTER</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-decoration: underline; font-size: .7rem; font-weight: 800; margin-top: -20px; color: #000;'>DESIGN & DEVELOPED BY MERCHANTSONS -  ( GIAIC - Monday 2pm to 5pm ROLL # 00037391 )</p>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: .8rem; font-weight: 800; margin-top: -20px; color: #000;'>Assignment Date :  February 26th 2025</p>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 20px; color: rgba(255, 255, 255, 0.85); margin-top: 0px;'>Convert between units with precision and ease</h1>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 13px; color: #000; margin-top: -20px;'>14 conversion categories covering all common unit types</p>", unsafe_allow_html=True)
        
        # Subtle divider
        st.markdown("<hr style='height: 1px; background-color: rgba(255, 255, 255, 0.3); border: none; margin: 15px 0px;'>", unsafe_allow_html=True)
        
        # Conversion categories with colorful selection
        categories = [
            "Length", "Area", "Volume", "Weight/Mass", "Temperature", 
            "Time", "Speed", "Pressure", "Energy", "Power",
            "Data Storage", "Angle", "Fuel Economy", "Frequency"
        ]
        
        # Category icons mapping
        category_icons = {
            "Length": "📏", "Area": "📐", "Volume": "🧊", "Weight/Mass": "⚖️", 
            "Temperature": "🌡️", "Time": "⏱️", "Speed": "🏎️", "Pressure": "🔍", 
            "Energy": "⚡", "Power": "💪", "Data Storage": "💾", "Angle": "📐",
            "Fuel Economy": "⛽", "Frequency": "〰️"
        }
        
        # Format category options with icons
        category_options = [f"{category_icons[cat]} {cat}" for cat in categories]
        
        # Create a styled selectbox for categories
        selected_category_with_icon = st.selectbox(
            "Select conversion category",
            category_options,
            index=0,
            key="category_selector"
        )
        
        # Extract the category name without the icon
        selected_category = selected_category_with_icon.split(" ", 1)[1]
        
        # Create card-like container for the converter with translucent background
        # st.markdown("""
        # <div style="background-color: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); margin-bottom: 20px;">
        # """, unsafe_allow_html=True)
        
        # Conversion units mapping
        conversion_units = {
            "Length": {
                "Kilometer (km)": 1000,
                "Meter (m)": 1,
                "Centimeter (cm)": 0.01,
                "Millimeter (mm)": 0.001,
                "Micrometer (μm)": 0.000001,
                "Nanometer (nm)": 0.000000001,
                "Mile (mi)": 1609.344,
                "Yard (yd)": 0.9144,
                "Foot (ft)": 0.3048,
                "Inch (in)": 0.0254,
                "Nautical mile (nmi)": 1852
            },
            "Area": {
                "Square kilometer (km²)": 1000000,
                "Square meter (m²)": 1,
                "Square centimeter (cm²)": 0.0001,
                "Square millimeter (mm²)": 0.000001,
                "Square mile (mi²)": 2589988.11,
                "Square yard (yd²)": 0.83612736,
                "Square foot (ft²)": 0.09290304,
                "Square inch (in²)": 0.00064516,
                "Hectare (ha)": 10000,
                "Acre (ac)": 4046.8564224
            },
            "Volume": {
                "Cubic meter (m³)": 1,
                "Cubic centimeter (cm³)": 0.000001,
                "Cubic millimeter (mm³)": 0.000000001,
                "Liter (L)": 0.001,
                "Milliliter (mL)": 0.000001,
                "US gallon (gal)": 0.00378541,
                "US quart (qt)": 0.000946353,
                "US pint (pt)": 0.000473176,
                "US cup": 0.000236588,
                "US fluid ounce (fl oz)": 0.0000295735,
                "US tablespoon (tbsp)": 0.0000147868,
                "US teaspoon (tsp)": 0.00000492892,
                "Imperial gallon (gal)": 0.00454609,
                "Imperial quart (qt)": 0.00113652,
                "Imperial pint (pt)": 0.000568261,
                "Imperial fluid ounce (fl oz)": 0.0000284131,
                "Cubic foot (ft³)": 0.0283168,
                "Cubic inch (in³)": 0.0000163871
            },
            "Weight/Mass": {
                "Tonne (t)": 1000,
                "Kilogram (kg)": 1,
                "Gram (g)": 0.001,
                "Milligram (mg)": 0.000001,
                "Microgram (μg)": 0.000000001,
                "Imperial ton": 1016.05,
                "US ton": 907.185,
                "Stone (st)": 6.35029,
                "Pound (lb)": 0.453592,
                "Ounce (oz)": 0.0283495,
                "Carat (ct)": 0.0002
            },
            "Temperature": {
                "Celsius (°C)": "celsius",
                "Fahrenheit (°F)": "fahrenheit",
                "Kelvin (K)": "kelvin"
            },
            "Time": {
                "Year (yr)": 31536000,
                "Month (avg)": 2628000,
                "Week (wk)": 604800,
                "Day (d)": 86400,
                "Hour (hr)": 3600,
                "Minute (min)": 60,
                "Second (s)": 1,
                "Millisecond (ms)": 0.001,
                "Microsecond (μs)": 0.000001,
                "Nanosecond (ns)": 0.000000001
            },
            "Speed": {
                "Meter per second (m/s)": 1,
                "Kilometer per hour (km/h)": 0.277778,
                "Mile per hour (mph)": 0.44704,
                "Foot per second (ft/s)": 0.3048,
                "Knot (kn)": 0.514444
            },
            "Pressure": {
                "Pascal (Pa)": 1,
                "Kilopascal (kPa)": 1000,
                "Bar": 100000,
                "Pound per square inch (psi)": 6894.76,
                "Atmosphere (atm)": 101325,
                "Millimeter of mercury (mmHg)": 133.322,
                "Inch of mercury (inHg)": 3386.39
            },
            "Energy": {
                "Joule (J)": 1,
                "Kilojoule (kJ)": 1000,
                "Calorie (cal)": 4.184,
                "Kilocalorie (kcal)": 4184,
                "Watt-hour (Wh)": 3600,
                "Kilowatt-hour (kWh)": 3600000,
                "Electronvolt (eV)": 1.602176634e-19,
                "British thermal unit (BTU)": 1055.06,
                "US therm": 105480400,
                "Foot-pound (ft⋅lb)": 1.35582
            },
            "Power": {
                "Watt (W)": 1,
                "Kilowatt (kW)": 1000,
                "Megawatt (MW)": 1000000,
                "Horsepower (hp)": 745.7,
                "BTU per hour": 0.29307
            },
            "Data Storage": {
                "Bit (b)": 0.125e-6,
                "Kilobit (kb)": 0.125e-3,
                "Megabit (Mb)": 0.125,
                "Gigabit (Gb)": 125,
                "Terabit (Tb)": 125000,
                "Byte (B)": 1e-6,
                "Kilobyte (KB)": 0.001,
                "Megabyte (MB)": 1,
                "Gigabyte (GB)": 1000,
                "Terabyte (TB)": 1000000
            },
            "Angle": {
                "Degree (°)": 1,
                "Radian (rad)": 57.2958,
                "Gradian (grad)": 0.9,
                "Minute of arc (′)": 1/60,
                "Second of arc (″)": 1/3600,
                "Revolution": 360
            },
            "Fuel Economy": {
                "Miles per gallon (mpg)": 1,
                "Miles per gallon (Imperial)": 0.832674,
                "Kilometer per liter (km/L)": 0.425144,
                "Liter per 100 kilometers (L/100km)": "inverse"
            },
            "Frequency": {
                "Hertz (Hz)": 1,
                "Kilohertz (kHz)": 1000,
                "Megahertz (MHz)": 1000000,
                "Gigahertz (GHz)": 1000000000
            }
        }
        
        # Get available units for the selected category
        available_units = list(conversion_units[selected_category].keys())
        
        # Create two columns with styled inputs
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<p style='margin-top: 20px; margin-bottom: -30px; font-weight: 500; color: white;'>From</p>", unsafe_allow_html=True)
            from_unit = st.selectbox("", available_units, key="from_unit")
            from_value = st.number_input("Value:", value=1.0, format="%.8f", key="from_value", 
                                         step=0.1)
        
        with col2:
            st.markdown("<p style='margin-top: 20px; margin-bottom: -30px; font-weight: 500; color: white;'>To</p>", unsafe_allow_html=True)
            to_unit = st.selectbox("", available_units, key="to_unit", index=1 if len(available_units) > 1 else 0)
        
        # Adding space before convert button
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        
        # Add a fancy conversion button
        _, btn_col, _ = st.columns([1, 2, 1])
        with btn_col:
            convert_button = st.button("Convert", 
                                      key="convert_button", 
                                      type="primary",
                                      use_container_width=True)
        
        # Perform conversion when button is clicked
        if convert_button:
            try:
                # Calculate conversion result
                result = convert_units(from_value, from_unit, to_unit, selected_category, conversion_units)
                
                # Create a stylish result card
                st.markdown("""
                <div style="background-color: rgba(255, 255, 255, 0.15); 
                            backdrop-filter: blur(10px); 
                            padding: 20px; 
                            border-radius: 10px; 
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
                            border: 1px solid rgba(255, 255, 255, 0.2); 
                            margin-top: 20px;
                            text-align: center;">
                """, unsafe_allow_html=True)
                
                # Display the result
                st.markdown(f"""
                <p style="color: white; font-size: 16px; margin-bottom: 5px;">Result:</p>
                <h2 style="color: white; font-weight: 600; margin-top: 0;">{from_value} {from_unit}</h2>
                <p style="color: white; font-size: 20px; margin: 10px 0;">equals</p>
                <h1 style="color: white; font-weight: 700; font-size: 28px;">{result:.8g} {to_unit}</h1>
                </div>
                """, unsafe_allow_html=True)
                
                # Add random fact based on category (optional fun feature)
                fun_facts = {
                    "Length": [
                        "Did you know? A light-year is about 9.5 trillion kilometers!",
                        "Fun fact: The average human height is about 1.7 meters.",
                    ],
                    "Weight/Mass": [
                        "Did you know? A teaspoon of a neutron star would weigh about 6 billion tons!",
                        "Fun fact: The average weight of an adult brain is about 1.4 kilograms.",
                    ],
                    "Temperature": [
                        "Did you know? The highest recorded temperature on Earth was 56.7°C in Death Valley, USA.",
                        "Fun fact: The average body temperature of a healthy human is about 37°C.",
                    ]
                }
                
                if selected_category in fun_facts:
                    st.markdown(f"""
                    <div style="text-align: center; margin-top: 20px; font-style: italic; color: rgba(255, 255, 255, 0.7);">
                    {random.choice(fun_facts[selected_category])}
                    </div>
                    """, unsafe_allow_html=True)
            
            except Exception as e:
                st.error(f"Error performing conversion: {e}")
        
        # Close the card container
        st.markdown("</div>", unsafe_allow_html=True)

def apply_custom_css():
    """Apply custom CSS styling to the app including the gradient background"""
    st.markdown("""
    <style>
        /* Remove top space */
        .block-container {
            padding-top: 10vmin;
            padding-bottom: 0px;
        }

        /* Background gradient */
        .stApp {
            background: linear-gradient(to bottom left, #4285F4, #003366) !important;
            background-attachment: fixed;
        }
        
        /* General styling for better contrast on dark background */
        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            color: white;
        }
        
        /* Streamlit container styling */
        .css-1d391kg, .css-1lsmgbg {
            background-color: transparent;
        }
        
        /* Input fields styling for dark theme */
        .stNumberInput input {
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            border-radius: 8px;
            padding: 10px 15px;
            height: auto;
        }
        
        .stNumberInput input:focus {
            border-color: white;
            box-shadow: 0 1px 2px rgba(255, 255, 255, 0.1);
        }
        
        /* Selectbox styling */
        .stSelectbox [data-baseweb="select"] {
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
        }
        
        .stSelectbox [data-baseweb="select"]:focus {
            border-color: white;
        }
        
        /* Dropdown menus */
        div[data-baseweb="popover"] div[data-baseweb="menu"] {
            background-color: #1a3c6b;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        div[data-baseweb="popover"] div[role="option"] {
            color: white;
        }
        
        div[data-baseweb="popover"] div[role="option"]:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        /* Button styling */
        .stButton button {
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.4);
            border-radius: 24px;
            font-weight: 500;
            font-size: 16px;
            padding: 12px 24px;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #163555;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
        }
        
        # /* Hide the Streamlit menu */
        # #MainMenu {visibility: hidden;}
        # footer {visibility: hidden;}
        # header {visibility: hidden;}
        
        /* Make inputs text white */
        .stTextInput input, .stTextInput textarea, .stNumberInput input {
            color: white;
        }
        
        /* Make selectbox text white */
        .stSelectbox [data-baseweb="select"] span {
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

def convert_units(value, from_unit, to_unit, category, conversion_units):
    """Convert value from one unit to another"""
    # Special case for temperature
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    # Special case for fuel economy when using L/100km
    if category == "Fuel Economy" and ("L/100km" in from_unit or "L/100km" in to_unit):
        return convert_fuel_economy(value, from_unit, to_unit, conversion_units[category])
    
    # For regular conversions
    from_factor = conversion_units[category][from_unit]
    to_factor = conversion_units[category][to_unit]
    
    # Calculate the conversion
    result = value * (from_factor / to_factor)
    
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature values between different scales"""
    # Extract the temperature scale from the unit names
    from_scale = from_unit.split()[0].lower()
    to_scale = to_unit.split()[0].lower()
    
    # Convert to Kelvin first (as an intermediate step)
    if from_scale == "celsius":
        kelvin = value + 273.15
    elif from_scale == "fahrenheit":
        kelvin = (value + 459.67) * 5/9
    else:  # Already in Kelvin
        kelvin = value
    
    # Convert from Kelvin to target scale
    if to_scale == "celsius":
        result = kelvin - 273.15
    elif to_scale == "fahrenheit":
        result = kelvin * 9/5 - 459.67
    else:  # Target is Kelvin
        result = kelvin
    
    return result

def convert_fuel_economy(value, from_unit, to_unit, conversion_factors):
    """Handle fuel economy conversions with special attention to L/100km"""
    # If converting from L/100km to another unit
    if "L/100km" in from_unit:
        # Convert to mpg (US) first
        mpg_us = 235.215 / value
        
        # Now convert to target unit
        if "mpg (Imperial)" in to_unit:
            return mpg_us / conversion_factors["Miles per gallon (Imperial)"]
        elif "km/L" in to_unit:
            return mpg_us / conversion_factors["Kilometer per liter (km/L)"]
        else:  # Target is mpg (US)
            return mpg_us
    
    # If converting to L/100km from another unit
    elif "L/100km" in to_unit:
        # Convert to mpg (US) first
        if "mpg (Imperial)" in from_unit:
            mpg_us = value * conversion_factors["Miles per gallon (Imperial)"]
        elif "km/L" in from_unit:
            mpg_us = value * conversion_factors["Kilometer per liter (km/L)"]
        else:  # Source is already mpg (US)
            mpg_us = value
            
        # Convert from mpg (US) to L/100km
        return 235.215 / mpg_us
    
    # Regular conversion between mpg (US), mpg (Imperial), and km/L
    else:
        from_factor = conversion_factors[from_unit]
        to_factor = conversion_factors[to_unit]
        return value * (from_factor / to_factor)

if __name__ == "__main__":
    main()
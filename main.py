import streamlit as st
import random
import time

# Custom CSS for cosmic styling and animations
st.markdown("""
    <style>
    * {
        font-family: 'Orbitron', sans-serif;
    }
    .stApp {
        background: linear-gradient(180deg, #1e1e2f 0%, #2b1b47 100%);
        color: #e0e0ff;  /* Default text color */
    }
    h1 {
        color: #ffcc00;
        text-align: center;
        animation: glow 2s infinite alternate;
    }
    .prediction-card {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid #ffcc00;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 0 15px #ffcc00;
        animation: fadeIn 1s ease-in;
    }
    .stButton>button {
        background-color: #ff3366;
        color: white;
        border-radius: 10px;
        padding: 12px 25px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #cc0052;
        transform: scale(1.1);
    }
    
    label, .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #fc23ef !important;  
        font-size: 16px;
    }
    
    .stTextInput input, .stNumberInput input, .stSelectbox div {
        color: #fc23ef !important;
    }
    @keyframes glow {
        0% { text-shadow: 0 0 5px #ffcc00; }
        100% { text-shadow: 0 0 20px #ffcc00; }
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    /* Starry background */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('https://www.transparenttextures.com/patterns/stardust.png');
        opacity: 0.3;
        z-index: -1;
    }
    </style>
""", unsafe_allow_html=True)

# Font import
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap" rel="stylesheet">', unsafe_allow_html=True)

# Title
st.title("🌌 Cosmic Fortune Teller 🌠")

# User inputs
st.write("Tell the cosmos about yourself...")
name = st.text_input("Your Name")
fav_number = st.number_input("Favorite Number (1-100)", min_value=1, max_value=100, value=1)
zodiac = st.selectbox("Your Zodiac Sign", [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
])

# Prediction logic
if st.button("Reveal My Cosmic Fate"):
    with st.spinner("🔮 Consulting the stars..."):
        time.sleep(1.5)  # Brief delay for dramatic effect
        
        # Random cosmic elements
        destinies = [
            "will conquer new galaxies",
            "shall dance with stardust",
            "is destined for cosmic greatness",
            "will unlock secrets of the void",
            "shall lead a meteor shower"
        ]
        cosmic_traits = [
            "infinite courage", "stellar wisdom", "lunar charm",
            "solar ambition", "nebula-like creativity"
        ]
        
        # Generate prediction
        destiny = random.choice(destinies)
        trait = random.choice(cosmic_traits)
        lucky_star = f"Star #{fav_number * random.randint(1, 10)}"
        prediction = f"{name}, the {zodiac}, {destiny} with {trait}. Your lucky star is {lucky_star}!"

        # Display in a glowing card
        st.markdown(f"""
            <div class='prediction-card'>
                <h3>Your Cosmic Fate</h3>
                <p>{prediction}</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #ffcc00;'>Created by Amjad Afza Ahmed 🚀</p>", unsafe_allow_html=True)
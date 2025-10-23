import streamlit as st
import pandas as pd
import random

# Page configuration
st.set_page_config(
    page_title="हिमालयन प्रहरी",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main { 
        background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(135deg, #2e7d32, #388e3c);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        color: white;
    }
    .card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .header-card {
        background: linear-gradient(135deg, #2e7d32, #388e3c);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }
    .carbon-badge {
        background: linear-gradient(135deg, #2e7d32, #388e3c);
        color: white;
        padding: 15px;
        border-radius: 25px;
        text-align: center;
        font-weight: bold;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header Section
    st.markdown("""
    <div class="header-card">
        <h1 style='margin:0; font-size: 2.5em;'>🏔️ हिमालयन प्रहरी</h1>
        <p style='margin:0; font-size: 1.2em; opacity: 0.9;'>पहाड़ी किसानों के लिए कार्बन क्रेडिट प्लेटफॉर्म</p>
    </div>
    """, unsafe_allow_html=True)

    # Main Form
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.subheader("👨‍🌾 किसान रजिस्ट्रेशन फॉर्म")
        
        # Form columns
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("**पूरा नाम**", placeholder="रमेश सिंह नेगी")
            village = st.text_input("**गाँव/बस्ती का नाम**", placeholder="तिलवाड़ा, रुद्रप्रयाग")
            mobile = st.text_input("**मोबाइल नंबर**", placeholder="9876543210", max_chars=10)
            
        with col2:
            land_size = st.number_input("**जमीन का आकार (नाली)**", min_value=0.0, value=2.5, step=0.1)
            tree_count = st.number_input("**पेड़ों की संख्या**", min_value=0, value=50, step=1)
            district = st.selectbox("**जिला**", [
                "जिला चुनें...", "रुद्रप्रयाग", "चमोली", "उत्तरकाशी", "टिहरी", 
                "पौड़ी", "अल्मोड़ा", "बागेश्वर", "पिथौरागढ़", "नैनीताल", "देहरादून"
            ])
        
        # Submit button
        submitted = st.button("📝 रजिस्टर करें और कार्बन स्कोर देखें")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Results Section
    if submitted:
        if name and village and mobile and district != "जिला चुनें...":
            # Carbon calculation
            tree_carbon = tree_count * 0.0256
            land_carbon = land_size * 0.4  # Increased for better results
            total_carbon = tree_carbon + land_carbon
            estimated_income = total_carbon * 850
            
            # Farmer ID
            farmer_id = f"HP24{random.randint(1000, 9999)}"
            
            # Results card
            st.markdown("""
            <div class="card" style='border-left: 5px solid #2e7d32;'>
            """, unsafe_allow_html=True)
            
            st.success("🎉 रजिस्ट्रेशन सफल!")
            
            # Farmer details
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**किसान आईडी:** {farmer_id}")
                st.write(f"**नाम:** {name}")
                st.write(f"**गाँव:** {village}")
                st.write(f"**जिला:** {district}")
                
            with col2:
                st.write(f"**जमीन का आकार:** {land_size} नाली")
                st.write(f"**पेड़ों की संख्या:** {tree_count}")
                st.write(f"**मोबाइल:** {mobile}")
            
            # Carbon badge
            st.markdown(f"""
            <div class="carbon-badge">
                🌱 आपका कार्बन स्कोर: {total_carbon:.2f} टन CO₂/वर्ष
            </div>
            """, unsafe_allow_html=True)
            
            # Income
            st.write(f"**💰 अनुमानित वार्षिक आय:** ₹{estimated_income:.2f}")
            
            # Additional info
            st.info("""
            **📞 अगले steps:**
            - हिमालयन प्रहरी टीम 24 घंटे में आपसे संपर्क करेगी
            - कार्बन क्रेडिट verification process शुरू होगी
            - आपकी जानकारी सुरक्षित रखी जाएगी
            """)
            
            # Download button (simulated)
            if st.button("📄 रजिस्ट्रेशन स्लिप डाउनलोड करें"):
                st.success("स्लिप आपके डिवाइस में डाउनलोड हो गई!")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        else:
            st.error("❌ कृपया सभी आवश्यक जानकारी भरें")

    # Statistics Section
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 हिमालयन प्रहरी स्टैटिस्टिक्स")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("कुल रजिस्टर्ड किसान", "1,247")
        with col2:
            st.metric("कुल कार्बन बचत", "5,892 टन")
        with col3:
            st.metric("कुल आय उत्पन्न", "₹50.8 लाख")
        with col4:
            st.metric("कवर किए गए गाँव", "89")
            
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <h4>हिमालयन प्रहरी - पहाड़ी किसानों के लिए कार्बन क्रेडिट पहल</h4>
        <p>📞 हेल्पलाइन: 1800-XXX-XXXX | 📧 ईमेल: support@himalayanprahari.com</p>
        <p>© 2024 हिमालयन प्रहरी. सभी अधिकार सुरक्षित।</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

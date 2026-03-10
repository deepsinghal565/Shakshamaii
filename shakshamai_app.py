"""
============================================
🛡️ SHAKSHAMAI - AI Predictive Maintenance
Made for Indian MSMEs | 100% Free & Open Source
============================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time
import random
import os

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="ShakshamAI - Predictive Maintenance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86C1;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #566573;
        font-size: 1.2rem;
        margin-top: 0;
    }
    .tagline {
        text-align: center;
        color: #2874A6;
        font-style: italic;
        font-size: 1.1rem;
    }
    .footer {
        text-align: center;
        color: #7F8C8D;
        font-size: 0.9rem;
        margin-top: 3rem;
    }
    .success-box {
        background-color: #D4EDDA;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #28A745;
    }
    .warning-box {
        background-color: #FFF3CD;
        color: #856404;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #FFC107;
    }
    .danger-box {
        background-color: #F8D7DA;
        color: #721C24;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #DC3545;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER SECTION
# ============================================

st.markdown('<p class="main-header">🛡️ SHAKSHAMAI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Predictive Maintenance for Indian MSMEs</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">"Shakti of Edge AI + Akshamta of Affordability"</p>', unsafe_allow_html=True)
st.markdown("---")

# ============================================
# LOAD MODEL
# ============================================

@st.cache_resource
def load_model():
    """Load the trained ShakshamAI model"""
    try:
        # Check if model file exists
        if os.path.exists('shakshamai_model.pkl'):
            model = joblib.load('shakshamai_model.pkl')
            return model, True
        else:
            return None, False
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, False

model, model_loaded = load_model()

# ============================================
# SIDEBAR - MACHINE CONFIGURATION
# ============================================

with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)
    st.markdown("## ⚙️ Control Panel")
    st.markdown("---")
    
    # Machine selection
    machine_id = st.selectbox(
        "Select Machine",
        ["CNC Machine - Unit 01", "CNC Machine - Unit 02", 
         "Conveyor Belt - Unit 03", "Packaging Unit - 04",
         "Hydraulic Press - 05", "Injection Molding - 06"]
    )
    
    st.markdown("---")
    
    # Alert settings
    st.markdown("### 🔔 Alert Settings")
    alert_method = st.multiselect(
        "Alert Method",
        ["LED", "Buzzer", "SMS", "Dashboard"],
        default=["Dashboard"]
    )
    
    threshold = st.slider("Alert Threshold (%)", 50, 90, 70)
    
    st.markdown("---")
    st.markdown("### 📊 Machine Stats")
    st.metric("Total Machines", "6", "+2 today")
    st.metric("Active Alerts", "3", "-1")
    st.metric("Uptime", "98.2%", "+0.3%")
    
    st.markdown("---")
    st.caption("🔋 Edge AI Device | Offline First | Made in India")

# ============================================
# MAIN CONTENT
# ============================================

if not model_loaded:
    # Model upload option
    st.warning("⚠️ ShakshamAI model not found. Please upload your trained model.")
    
    with st.expander("📤 Upload Model", expanded=True):
        st.markdown("""
        **How to get model?**
        1. Train model in Google Colab using our code
        2. Download shakshamai_model.pkl
        3. Upload here
        """)
        
        uploaded_file = st.file_uploader("Choose shakshamai_model.pkl", type=['pkl'])
        
        if uploaded_file is not None:
            model = joblib.load(uploaded_file)
            model_loaded = True
            st.success("✅ ShakshamAI model loaded successfully!")
            st.balloons()
else:
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Manual Analysis", "📈 Live Monitoring", "📊 Analytics", "ℹ️ About"])
    
    # ============================================
    # TAB 1: MANUAL ANALYSIS
    # ============================================
    
    with tab1:
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("### 🔧 Manual Sensor Input")
            st.markdown("Enter current machine parameters for instant analysis")
            
            # Input form
            with st.form("manual_input"):
                row1 = st.columns(3)
                with row1[0]:
                    air_temp = st.number_input("🌡️ Air Temperature (K)", 
                                               min_value=290.0, max_value=320.0, 
                                               value=298.0, step=0.5,
                                               help="Normal range: 295-305K")
                with row1[1]:
                    process_temp = st.number_input("🔥 Process Temperature (K)", 
                                                    min_value=300.0, max_value=340.0, 
                                                    value=310.0, step=0.5)
                with row1[2]:
                    speed = st.number_input("⚡ Rotational Speed (rpm)", 
                                            min_value=1000, max_value=2500, 
                                            value=1500, step=10)
                
                row2 = st.columns(3)
                with row2[0]:
                    torque = st.number_input("🔧 Torque (Nm)", 
                                             min_value=10.0, max_value=100.0, 
                                             value=40.0, step=0.5)
                with row2[1]:
                    tool_wear = st.number_input("⏱️ Tool Wear (min)", 
                                                min_value=0, max_value=500, 
                                                value=200, step=5)
                with row2[2]:
                    st.markdown("<br>", unsafe_allow_html=True)
                    submitted = st.form_submit_button("🛡️ Analyze with ShakshamAI", 
                                                       type="primary", 
                                                       use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Quick Stats")
            st.markdown("Current machine: **" + machine_id + "**")
            st.markdown("Last maintenance: **2 days ago**")
            st.markdown("Operator: **Rajesh Kumar**")
            st.markdown("Shift: **Morning (6AM-2PM)**")
            
            st.markdown("---")
            st.markdown("### ⚠️ Recent Alerts")
            st.info("🔵 No recent alerts for this machine")
        
        if submitted:
            with st.spinner("🛡️ ShakshamAI analyzing machine health..."):
                time.sleep(1.5)  # Simulate processing
                
                # Prepare data for prediction
                input_data = pd.DataFrame([[air_temp, process_temp, speed, torque, tool_wear]],
                                         columns=['Air temperature [K]', 'Process temperature [K]',
                                                'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])
                
                # Make prediction
                prediction = model.predict(input_data)[0]
                probability = model.predict_proba(input_data)[0][1]
                
                # Display results
                st.markdown("---")
                st.markdown("### 🔍 Analysis Results")
                
                result_col1, result_col2 = st.columns(2)
                
                with result_col1:
                    # Gauge chart
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number+delta",
                        value=probability * 100,
                        title={'text': "Failure Risk (%)"},
                        delta={'reference': 70},
                        gauge={
                            'axis': {'range': [0, 100], 'tickwidth': 1},
                            'bar': {'color': "darkred" if prediction == 1 else "darkgreen"},
                            'steps': [
                                {'range': [0, 30], 'color': "#90EE90"},
                                {'range': [30, 70], 'color': "#FFD700"},
                                {'range': [70, 100], 'color': "#FFB6C1"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': threshold
                            }
                        }
                    ))
                    fig.update_layout(height=300, margin=dict(l=30, r=30, t=50, b=30))
                    st.plotly_chart(fig, use_container_width=True)
                
                with result_col2:
                    if prediction == 1:
                        st.markdown('<div class="danger-box">', unsafe_allow_html=True)
                        st.markdown("### ⚠️ CRITICAL ALERT!")
                        st.markdown(f"**Failure Probability: {probability:.1%}**")
                        st.markdown("🚨 **Immediate maintenance required!**")
                        st.markdown("📋 **Recommended Action:** Stop machine and inspect")
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        st.markdown("### ✅ Machine is HEALTHY")
                        st.markdown(f"**Failure Probability: {probability:.1%}**")
                        st.markdown("📋 **Recommended Action:** Continue normal operation")
                        st.markdown("</div>", unsafe_allow_html=True)
                
                # Recommendations
                st.markdown("### 📋 Detailed Recommendations")
                
                if probability < 0.3:
                    st.success("🟢 **Low Risk** - Machine operating normally. Next check in 7 days.")
                elif probability < 0.7:
                    st.warning("🟡 **Medium Risk** - Schedule maintenance within 48 hours.")
                else:
                    st.error("🔴 **High Risk** - Immediate action required. Stop machine and inspect.")
                
                # Feature importance
                st.markdown("### 🔑 Key Factors")
                factors = {
                    "Temperature": air_temp / 310 * 100,
                    "Vibration": torque / 80 * 100,
                    "Tool Wear": tool_wear / 500 * 100,
                    "Speed": speed / 2000 * 100
                }
                
                factors_df = pd.DataFrame([
                    {"Factor": k, "Value": v} for k, v in factors.items()
                ])
                
                fig2 = px.bar(factors_df, x="Factor", y="Value", 
                             title="Sensor Readings (% of threshold)",
                             color="Value", color_continuous_scale=["green", "yellow", "red"])
                st.plotly_chart(fig2, use_container_width=True)
    
    # ============================================
    # TAB 2: LIVE MONITORING
    # ============================================
    
    with tab2:
        st.markdown("### 📡 Real-time Machine Monitoring")
        st.markdown("Simulating live sensor data stream...")
        
        col1, col2, col3, col4 = st.columns(4)
        metrics_placeholder = st.empty()
        chart_placeholder = st.empty()
        alert_placeholder = st.empty()
        
        if st.button("▶️ Start Live Monitoring", type="primary"):
            # Create placeholders for live updates
            live_metrics = st.empty()
            live_chart = st.empty()
            live_alerts = st.empty()
            
            # Initialize data storage
            history = []
            
            # Simulate 20 readings
            for i in range(20):
                # Generate realistic sensor data
                temp = random.uniform(295, 315)
                process = random.uniform(305, 325)
                speed_val = random.uniform(1400, 1800)
                torque_val = random.uniform(30, 70)
                wear_val = random.uniform(100, 400)
                
                # 20% chance of anomaly
                if random.random() > 0.8:
                    temp += 8
                    torque_val += 15
                    status = "⚠️ ANOMALY"
                else:
                    status = "✅ NORMAL"
                
                # Predict
                input_data = pd.DataFrame([[temp, process, speed_val, torque_val, wear_val]],
                                         columns=['Air temperature [K]', 'Process temperature [K]',
                                                'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])
                pred = model.predict(input_data)[0]
                prob = model.predict_proba(input_data)[0][1]
                
                # Store history
                history.append({
                    'time': i,
                    'risk': prob,
                    'temp': temp,
                    'torque': torque_val
                })
                
                # Update metrics
                with live_metrics.container():
                    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
                    mcol1.metric("Temperature", f"{temp:.1f}K", 
                                "⚠️ High" if temp > 310 else "Normal")
                    mcol2.metric("Torque", f"{torque_val:.1f}Nm",
                                "⚠️ High" if torque_val > 60 else "Normal")
                    mcol3.metric("Risk", f"{prob:.1%}",
                                "🔴" if prob > 0.7 else "🟢")
                    mcol4.metric("Status", status)
                
                # Update chart
                df_hist = pd.DataFrame(history)
                live_chart.line_chart(df_hist.set_index('time')['risk'])
                
                # Show alert if anomaly
                if pred == 1:
                    live_alerts.error(f"⏰ {datetime.now().strftime('%H:%M:%S')} - ⚠️ ALERT! Failure risk: {prob:.1%}")
                elif prob > 0.5:
                    live_alerts.warning(f"⏰ {datetime.now().strftime('%H:%M:%S')} - ⚠️ Warning: Risk increasing")
                
                time.sleep(1.5)
            
            live_alerts.success("✅ Monitoring complete. ShakshamAI analyzed 20 cycles.")
    
    # ============================================
    # TAB 3: ANALYTICS
    # ============================================
    
    with tab3:
        st.markdown("### 📊 Machine Health Analytics")
        
        # Generate sample historical data
        dates = pd.date_range(start='2026-03-01', end='2026-03-10', freq='D')
        risk_data = [random.uniform(0.1, 0.9) for _ in range(len(dates))]
        
        df_history = pd.DataFrame({
            'Date': dates,
            'Risk Score': risk_data
        })
        
        # Risk trend chart
        fig3 = px.line(df_history, x='Date', y='Risk Score', 
                       title='Machine Risk Trend - Last 10 Days',
                       markers=True)
        fig3.add_hline(y=0.7, line_dash="dash", line_color="red", 
                       annotation_text="Alert Threshold")
        st.plotly_chart(fig3, use_container_width=True)
        
        # Statistics
        col1, col2, col3 = st.columns(3)
        col1.metric("Avg Risk", f"{np.mean(risk_data):.1%}", "-2%")
        col2.metric("Peak Risk", f"{max(risk_data):.1%}", "Yesterday")
        col3.metric("Alerts Triggered", "3", "-1")
        
        # Maintenance recommendations
        st.markdown("### 🔧 Maintenance Schedule")
        
        maint_data = pd.DataFrame({
            'Machine': ['CNC-01', 'CNC-02', 'Conveyor-03', 'Packaging-04'],
            'Last Maintenance': ['2026-03-05', '2026-03-01', '2026-02-28', '2026-03-07'],
            'Risk Level': ['Low', 'High', 'Medium', 'Low'],
            'Recommended Action': ['Check in 7 days', 'Immediate', 'Check in 2 days', 'Check in 10 days']
        })
        
        st.dataframe(maint_data, use_container_width=True)
    
    # ============================================
    # TAB 4: ABOUT
    # ============================================
    
    with tab4:
        st.markdown("### 🛡️ About ShakshamAI")
        
        st.markdown("""
        **ShakshamAI** is an AI-powered predictive maintenance solution designed specifically for Indian MSMEs.
        
        #### 🎯 Problem We Solve
        - 70% MSMEs face unplanned machine downtime
        - ₹60,000 Crore annual loss to Indian economy
        - Existing solutions too expensive (₹5-15 lakhs)
        - Internet dependency in Tier-2/3 cities
        
        #### 💡 Our Solution
        - Edge AI - Works without internet
        - Affordable - ₹5,000-8,000 only (95% cheaper)
        - Real-time monitoring & alerts
        - Made for India
        
        #### 🔬 Technology
        - ML Model: Random Forest (92% accuracy)
        - Edge Device: Raspberry Pi compatible
        - Dashboard: Streamlit (free hosting)
        - Alerts: LED/Buzzer/SMS
        
        #### 📊 Impact
        - 7.5 crore MSMEs target market
        - ₹3,750 Crore market opportunity
        - 50% reduction in downtime
        - 30% cost savings
        
        #### 👥 Team
        [STACK STORM]
        [KRCHE]
        
        #### 📞 Contact
        Email: [your-email]
        GitHub: [your-github]
        """)
        
        st.markdown("---")
        st.markdown("### 📁 Project Links")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("[![GitHub](https://img.icons8.com/color/48/000000/github.png)](https://github.com/yourusername/shakshamai)")
            st.markdown("**GitHub**")
        with col2:
            st.markdown("[![Streamlit](https://img.icons8.com/color/48/000000/streamlit.png)](https://shakshamai.streamlit.app)")
            st.markdown("**Live Demo**")
        with col3:
            st.markdown("[![Drive](https://img.icons8.com/color/48/000000/google-drive.png)](https://drive.google.com)")
            st.markdown("**Demo Video**")

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown("""
<div class="footer">
    🛡️ ShakshamAI | Made for India's MSMEs | 100% Free & Open Source<br>
    <small>Edge AI | Offline First | Affordable | Scalable</small><br>
    <small>© 2026 Team [Your Name] | All Rights Reserved</small>
</div>
""", unsafe_allow_html=True)
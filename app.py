import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Urban Waste Analytics", page_icon="🗑️", layout="wide")

st.markdown("""
    <style>
    .bin-card { padding: 20px; border-radius: 10px; text-align: center; font-weight: bold; }
    .status-critical { background-color: #e74c3c; color: white; }
    .status-ok { background-color: #2ecc71; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏙️ Smart Waste Management Dashboard")

if 'bin_history' not in st.session_state:
    st.session_state.bin_history = pd.DataFrame(columns=['Time', 'Fill_Level'])

placeholder = st.empty()

for _ in range(100):
    # Simulated Fill Level (0% to 100%)
    fill = round(np.random.uniform(10, 95), 1)
    
    new_data = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), fill]], 
                            columns=st.session_state.bin_history.columns)
    st.session_state.bin_history = pd.concat([st.session_state.bin_history, new_data]).tail(15)

    with placeholder.container():
        c1, c2, c3 = st.columns(3)
        c1.metric("Current Fill Level", f"{fill}%", delta="CRITICAL" if fill > 85 else "NORMAL")
        c2.metric("Est. Collection Time", "2 Hours" if fill > 80 else "Next Cycle")
        c3.metric("Bin Status", "ACTIVE")

        if fill > 85:
            st.markdown('<div class="bin-card status-critical">🚨 ACTION REQUIRED: BIN NEAR OVERFLOW</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="bin-card status-ok">✅ STATUS: BIN CAPACITY OPTIMAL</div>', unsafe_allow_html=True)

        fig = go.Figure(go.Indicator(
            mode = "gauge+number", value = fill,
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "red" if fill > 85 else "green"}},
            title = {'text': "Bin Capacity Used (%)"}
        ))
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(2)

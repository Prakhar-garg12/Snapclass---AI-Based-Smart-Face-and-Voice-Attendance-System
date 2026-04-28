import streamlit as st

def footer_home():

    logo_url = "https://dummyimage.com/600x200/5865F2/ffffff&text=Prakhar"

    st.markdown(f"""
    <div style="margin-top: 2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:white"> Created by  </p>
            <img src = '{logo_url}' style='max-height: 25px' />
    </div>        
     
                
""", unsafe_allow_html=True)


def footer_dashboard():

    logo_url = "https://dummyimage.com/600x200/5865F2/ffffff&text=Prakhar"

    st.markdown(f"""
    <div style="margin-top: 2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:black"> Created by  </p>
            <img src = '{logo_url}' style='max-height: 25px' />
    </div>        
     
                
""", unsafe_allow_html=True)

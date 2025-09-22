import streamlit as st

def render_header():
    st.markdown(
        """
        <div style="background: linear-gradient(90deg, #4CAF50, #2E7D32); 
                    padding: 1rem; border-radius: 10px; text-align: center; color: white;">
            <h1>🚀 K-Path Career Platform</h1>
            <p>AI-powered career guidance and recruitment made simple.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_footer():
    st.markdown(
        """
        <div style="margin-top: 2rem; padding: 1rem; text-align: center; 
                    background: #004d40; color: white; border-radius: 10px;">
            <p>© 2025 K-Path Career Platform | Built with ❤️ using 
            <a href="https://streamlit.io/" target="_blank" style="color:#ffcc80; text-decoration:none;">Streamlit</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

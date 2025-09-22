import streamlit as st

def add_header():
    st.markdown(
        """
        <div style="background-color:#0d6efd;padding:15px;border-radius:8px;margin-bottom:20px;">
            <h2 style="color:white;text-align:center;margin:0;">🚀 K-Path Career Platform</h2>
            <p style="color:white;text-align:center;margin:0;">AI-powered career guidance & recruitment made simple</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Back to Home button
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")


def add_footer():
    st.markdown(
        """
        <hr>
        <div style="text-align:center;color:gray;font-size:14px;">
            © 2025 K-Path Career Platform | Built with ❤️ using Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

import streamlit as st
from pathlib import Path
import sys
from src.user_profile_db_manager import UserProfileDBManager
# Ensure src is importable as a module named `user_profile_db_manager`
#sys.path.append(str(Path(__file__).parent / "src"))
#import user_profile_db_manager as db

st.set_page_config(page_title="Email System", page_icon="✉️", layout="wide")

st.markdown("# ✉️ Welcome to the Email Toolkit")
st.write(
    "A small app to manage profiles, user profiles and message templates. Use the sidebar to navigate pages."
)

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Manage contacts, templates and operator profiles")
    st.write(
        "This workspace stores small JSON-backed databases for quick prototyping. "
        "Click any page in the left sidebar to add, view or delete records."
    )

    st.subheader("Quick actions")
    if st.button("Show all profiles"):
        manager = UserProfileDBManager()
        profiles = manager.get_all_profiles()
        if profiles:
            st.dataframe(profiles)
        else:
            st.info("No profiles found.")
        manager.close()

with col2:
    st.image(
        "https://images.unsplash.com/photo-1520975919282-7b3c9df1ca2d?q=80&w=400&auto=format&fit=crop&ixlib=rb-4.0.3&s=1d3f9b2f6f2e6a7d3b2a1a4c5d6e7f8a",
        caption="Manage your profiles & templates",
    )

st.markdown("---")
st.write("Need help? See the README or open `email_system.json` to inspect stored data.")

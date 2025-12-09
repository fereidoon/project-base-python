import streamlit as st
from pathlib import Path
import sys
import pandas as pd
from src.user_profile_db_manager import UserProfileDBManager
# Make src importable as `user_profile_db_manager`
#sys.path.append(str(Path(__file__).parent.parent / "src"))
#import user_profile_db_manager as db

st.set_page_config(page_title="Profiles", page_icon="👥")

st.title("Profiles")
st.write("Create and manage simple contact profiles.")

manager = UserProfileDBManager()


with st.form("add_profile_form"):
    st.subheader("Add New Profile")
    name = st.text_input("Name")
    email = st.text_input("Email")
    title = st.text_input("Title")
    profession = st.text_input("Profession")
    submitted = st.form_submit_button("Create")

    if submitted:
        try:
            doc = manager.create_profile(name=name, email=email, title=title, profession=profession)
            st.success(f"Created profile for {doc.get('name')}")
        except Exception as e:
            st.error(f"Error creating profile: {e}")

st.markdown("---")
st.subheader("All Profiles")
profiles = manager.get_all_profiles()
if profiles:
    df = pd.DataFrame(profiles)
    st.dataframe(df)

    st.markdown("**Delete a profile**")
    emails = [p.get("email") for p in profiles if p.get("email")]
    to_delete = st.selectbox("Select email to delete", options=[""] + emails)
    if to_delete:
        if st.button("Delete"):
            ok = manager.delete_profile_by_email(to_delete)
            if ok:
                st.success(f"Deleted profile {to_delete}")
            else:
                st.error("Failed to delete — profile not found")
else:
    st.info("No profiles yet — add one above.")

manager.close()

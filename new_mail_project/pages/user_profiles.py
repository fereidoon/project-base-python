import streamlit as st
from pathlib import Path
import sys
import pandas as pd
from src.user_profile_db_manager import UserProfileDBManager
# Make src importable
#sys.path.append(str(Path(__file__).parent.parent / "src"))
#import user_profile_db_manager as db

st.set_page_config(page_title="User Profiles", page_icon="🧑‍💼")

st.title("User Profiles")
st.write("Create and manage comprehensive user profiles.")

manager = UserProfileDBManager()

with st.form("add_user_profile"):
    st.subheader("Add Detailed User Profile")
    name = st.text_input("Name")
    degree = st.text_input("Degree")
    profession = st.text_input("Profession")
    university = st.text_input("University")

    st.markdown("---")
    st.write("Optional contact / social fields")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("Github")
    x = st.text_input("X (Twitter) handle")
    personal_website = st.text_input("Personal Website")
    email = st.text_input("Email")
    signature = st.text_area("Signature", height=120)

    submitted = st.form_submit_button("Create User Profile")
    if submitted:
        try:
            doc = manager.create_user_profile(
                name=name,
                degree=degree,
                profession=profession,
                university=university,
                linkedin=linkedin,
                github=github,
                x=x,
                personal_website=personal_website,
                email=email,
                signature=signature,
            )
            st.success(f"Created user profile for {doc.get('name')}")
        except Exception as e:
            st.error(f"Error creating user profile: {e}")

st.markdown("---")
st.subheader("All User Profiles")
items = manager.list_all_user_profiles()
if items:
    df = pd.DataFrame(items)
    st.dataframe(df)

    st.markdown("**Delete a user profile**")
    emails = [u.get("email") for u in items if u.get("email")]
    to_delete = st.selectbox("Select email to delete", options=[""] + emails)
    if to_delete:
        if st.button("Delete"):
            ok = manager.delete_user_profile_by_email(to_delete)
            if ok:
                st.success(f"Deleted user profile {to_delete}")
            else:
                st.error("Failed to delete — user profile not found")
else:
    st.info("No user profiles yet — add one above.")

manager.close()

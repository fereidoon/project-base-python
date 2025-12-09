import streamlit as st
from pathlib import Path
import sys
import pandas as pd
from src.user_profile_db_manager import UserProfileDBManager
# Make src importable
#sys.path.append(str(Path(__file__).parent.parent / "src"))
#import user_profile_db_manager as db

st.set_page_config(page_title="Templates", page_icon="🧾")

st.title("Templates")
st.write("Create and manage message templates.")

manager = UserProfileDBManager()

with st.form("add_template_form"):
    st.subheader("Add Template")
    name = st.text_input("Template Name")
    body = st.text_area("Body", height=200)
    submitted = st.form_submit_button("Create Template")

    if submitted:
        try:
            doc = manager.create_template(name=name, body=body)
            st.success(f"Created template '{doc.get('name')}'")
        except Exception as e:
            st.error(f"Error creating template: {e}")

st.markdown("---")
st.subheader("All Templates")
templates = manager.list_all_templates()
if templates:
    df = pd.DataFrame(templates)
    st.dataframe(df)

    st.markdown("**Delete a template**")
    names = [t.get("name") for t in templates if t.get("name")]
    to_delete = st.selectbox("Select template to delete", options=[""] + names)
    if to_delete:
        if st.button("Delete"):
            ok = manager.delete_template_by_name(to_delete)
            if ok:
                st.success(f"Deleted template '{to_delete}'")
            else:
                st.error("Failed to delete — template not found")
else:
    st.info("No templates yet — add one above.")

manager.close()

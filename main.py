import streamlit as st
from libs import Library, Member

st.title("Library System")

if "library" not in st.session_state:
    st.session_state.library = Library("My Library")

page = st.sidebar.selectbox("Menu",["Add Member", "Manage Membership", "View Members"])

if page == "Add Member":
    st.write("### Add Member")
    name = st.text_input("Name")
    button = st.button("Add member")

    if button:
        new_member = Member(name)
        st.session_state.library.register_member(new_member)

elif page ==  "Manage Membership":
    st.write("### Manage membership")

    for index, member in enumerate(st.session_state.library.members):
        status = "active" if member.is_active else "not active"
        
        st.write(f"{member.name}")
        st.write(f"Status: {status}")
        deactivate_btn = st.button("Deactivate", key=f"deactivate_{index}")

        if deactivate_btn:
            member.deactivate()
            st.rerun()

elif page ==  "View Members":
    st.write("### View Active Members")
    
    active_members = st.session_state.library.get_active_members()

    if not active_members:
        st.write("No active member")
    
    else:

        for member in active_members:
            st.write(member)

print(st.session_state.library.members)
import streamlit as st
from dependancies import login_in, sign_up, home_page


def main():
    # st.session_state["take_me_to_signup"] = False
    # st.session_state["take_me_2login"] = False
    # st.session_state["take_2_homepage"] = False
    if "take_me_to_signup" in st.session_state and st.session_state["take_me_to_signup"]:
        sign_up()
    elif "take_me_2login" in st.session_state and st.session_state["take_me_2login"]:
        login_in()
    elif "take_2_homepage" in st.session_state and st.session_state["take_2_homepage"]:
        home_page()
    else:
        login_in()


if __name__ == "__main__":
    main()

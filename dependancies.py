import streamlit as st
import streamlit_authenticator as stauth
import time
import json
import functions


# home page
def home_page():
    st.session_state["take_me_to_signup"] = False
    st.session_state["take_me_2login"] = False
    name = st.session_state["name_of_user"]
    st.title(f"Welcome {name}")
    st.subheader("Web app is still under construction")
    st.header("Hey beautiful one ❤️😍, i ain't had no sleep since last night "
              "lol, i was soo geeked up on what i had doing")
    with st.sidebar.expander("Cool Apps"):
        st.write("check")


# authenticate users email and password
def authenticate_user(email, password):
    no_of_users, database = count_users()
    for box_item in database:
        for keys, values in box_item.items():
            if values["email"] == email and values["password"] == password:
                st.session_state["name_of_user"] = values["name"]
                return True
            else:
                return False


# functions to count users in database, returns int / List
def count_users():
    with open("d_base.json", "r") as db:
        data_base = json.load(db)
        return len(data_base), data_base


# inserts sign up data into database
def insert_credential(name, email, password):
    num_of_users, data_base = count_users()
    data_base.append(
        {num_of_users + 1:
             {"name": name, "email": email, "password": password}
         }
    )
    with open("d_base.json", "w") as dbs:
        json.dump(data_base, dbs)


def sign_up():
    st.subheader(":green[Signup]")
    with st.form(key='signup', clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            si_fname = st.text_input("First name", placeholder="Fname", key="si_fname")
            si_email = st.text_input("Email", placeholder="Email", key="si_email")
            si_gender = st.selectbox("Choose Gender", ("Male", "Female"),
                                     index=None, placeholder="Gender", )
        with col2:
            si_lname = st.text_input("Last name", placeholder="Lname", key="si_lname")
            si_password = st.text_input("Password", placeholder="Password", key="si_password", type="password")
            si_country = st.selectbox("Choose Country",
                                      ("Ghana", "Canada", "United States"),
                                      index=None, placeholder="Gender")

        if st.form_submit_button("Create account"):
            check_boolean = {
                "si_fname": False,
                "si_email": False,
                "si_lname": False,
                "si_password": False,
            }
            key_name = ["si_fname", "si_email",
                        "si_lname", "si_password"]

            for dt in key_name:
                if st.session_state[f"{dt}"]:
                    check_boolean[f"{dt}"] = True
            if all(check_boolean.values()):
                insert_credential(f"{si_fname} {si_lname}", si_email, si_password)
                st.success("Account created successfully")
                st.session_state["take_me_2login"] = True
                st.session_state["take_me_to_signup"] = False
                st.balloons()
                st.experimental_rerun()
            else:
                st.warning("Oops something went wrong, cross check the forms 🤔")


def login_in():
    st.header("Log in")
    with st.form(key="signin", clear_on_submit=False):
        log_email = st.text_input("Email", placeholder="Email")
        log_password = st.text_input("Password", placeholder="Password", type="password")
        coll1, coll2 = st.columns(2)

        if coll1.form_submit_button("Login Now"):
            if log_email and log_password:
                if authenticate_user(log_email, log_password):
                    st.balloons()
                    st.session_state["take_me_2login"] = False
                    st.session_state["take_me_to_signup"] = False
                    st.session_state["take_2_homepage"] = True
                    st.experimental_rerun()
                else:
                    st.warning("wrong email or password")
            else:
                st.warning("Enter email and password")



        if coll2.form_submit_button("Signup Now"):
            st.session_state["take_me_to_signup"] = True
            st.experimental_rerun()

        # session_state
        # st.write(st.session_state)

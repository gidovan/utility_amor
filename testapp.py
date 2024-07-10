import json
import streamlit as st


def count_users():
    with open("d_base.json", "r") as db:
        data_base = json.load(db)
        return len(data_base), data_base



def authenticate_user(email, password):
    no_of_users, database = count_users()
    for box_item in database:
        for keys, values in box_item.items():
            if values["email"] == email and values["password"] == password:
                st.session_state["name_of_user"] = values["name"]
                return True
            else:
                return False



# number, data = count_users()
# print(number)
# print(data)

print(authenticate_user("wd@gmail.com", "pass12"))
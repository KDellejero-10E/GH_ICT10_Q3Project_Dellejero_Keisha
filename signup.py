from pyscript import Element

def create_account():
    username = Element("username").value
    password = Element("password").value

    if username and password:
        Element("message").write(
            "Account created successfully."
        )
    else:
        Element("message").write(
            "Please complete all fields."
        )
from pyscript import Element

def create_account():
    username = Element("username").value
    password = Element("password").value

    if username and password:
        Element("message").element.innerHTML = "Account created successfully."
    else:
        Element("message").element.innerHTML = "Please complete all fields."
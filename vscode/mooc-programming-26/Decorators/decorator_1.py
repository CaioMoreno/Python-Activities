def authorized(func):

    def wrapper(username, password):
        if username in authorized_users.keys():
            if password == authorized_users[username]:
                return func(username, password)
            return "Not authorized!"
    return wrapper

@authorized
def get_me(username, password):
    return "MEEEEEE"

@authorized
def get_comments(username, password):
    return "YEAHHHH"

authorized_users = {"caio": "1234", "lulu": "1432", "papai": "5678", "mamae": "4789"}
print(get_comments("caio", "1234"))
print(get_me("lulu", "123"))
from flask_login import LoginManager, login_required

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) # Fetch the user from the database


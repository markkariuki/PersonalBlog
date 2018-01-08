from app import create_app,db
from flask_script import Manager,Server
from app.models import User

#creating the app instance
app = create_app ('development')


Manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    app.run()

import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import blueprint
from app.main import create_app, db
from app.main.setup_db import setup_petKindList

app = create_app("dev")
app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

@manager.command
def populate_db():
    setup_petKindList()

@manager.command
def run():
    app.run()

@manager.command
def test():
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0

    return 1

if __name__ == "__main__":
    manager.run()

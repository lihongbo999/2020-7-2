from flask_script import Manager, Server
import main
import models1
from flask_migrate import Migrate, MigrateCommand

# Init manager object via app object
manager = Manager(main.app)

# Init migrate object via app and db object
migrate = Migrate(main.app, models1.db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server",Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=main.app,
                db=models1.db,
                User=models1.User,
                Post=models1.Post,
                Comment=models1.Comment,
                Tag=models1.Tag
                )
if __name__ == '__main__':
    manager.run()

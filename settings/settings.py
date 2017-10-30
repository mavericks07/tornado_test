import tornado.options
from tornado.options import options, define
from playhouse.db_url import connect
print("settings")

define('env', default='dev', help='env', type=str)
define('DB_HOST', default='127.0.0.1', type=str)
define('DB_USERNAME', default='root', type=str)
define('DB_PASSWORD', default='qw010203', type=str)
define('DB_NAME', default='apistar', type=str)
define('DB_MAX_CONNECTION', default=100, type=int)
define('DB_STALE_TIMEOUT', default=300, type=int)

tornado.options.parse_command_line()
if options.env == 'dev':
    tornado.options.parse_config_file('settings/base.py')
elif options.env == 'prod':
    tornado.options.parse_config_file('settings/prod.py')
else:
    tornado.options.parse_config_file('settings/base.py')


db = connect(f'mysql+pool://{options.DB_USERNAME}:{options.DB_PASSWORD}@{options.DB_HOST}/{options.DB_NAME}'
             f'?max_connections={options.DB_MAX_CONNECTION}&stale_timeout={options.DB_STALE_TIMEOUT}')

print(db)
# Current network
NETWORK_NAME = 'net3'

# Disable stdout logging
enableStdOutLogging = False

# Directory to store ledger.
LEDGER_DIR = '/var/lib/indy'

# Directory to store logs.
LOG_DIR = '/var/log/indy'

# Directory to store keys.
KEYS_DIR = '/var/lib/indy'

# Directory to store genesis transactions files.
GENESIS_DIR = '/var/lib/indy'

# Directory to store backups.
BACKUP_DIR = '/var/lib/indy/backup'

# Directory to store plugins.
PLUGINS_DIR = '/var/lib/indy/plugins'

# Directory to store node info.
NODE_INFO_DIR = '/var/lib/indy'


ENABLED_PLUGINS=[]

ENABLED_PLUGINS.append('sovtoken')

ENABLED_PLUGINS.append('sovtokenfees')

ANYONE_CAN_WRITE = False

UPGRADE_ENTRY = 'sovrin'

INDY_VERSION_MATCHING = {"1.1.52": "1.9.1", "1.1.24": "0.9.3", "1.1.35": "0.9.3", "1.1.50": "1.0.0"}

from flask import Flask
from flask import escape,send_from_directory
import yaml
import os

app = Flask(__name__)

app.config.from_object(os.getenv('DYN_IPXE_CONFIG_MODULE', 'config'))

# Load MAC association file
with open(app.config["MAC_ASSOCIATION_FILE"], 'r') as f:
    mac_assoc = yaml.load(f, yaml.SafeLoader)

@app.route("/<mac>")
def boot_sequence(mac):
    return send_from_directory(
        app.config["IPXE_BOOT_SCRIPTS_DIRECTORY"], mac_assoc[mac]
    )

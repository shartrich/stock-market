import sshtunnel
from utils.configs.settings import SSH_HOST, SSH_USER, SSH_PASS, SSH_PORT, SQL_IP, SQL_HOSTNAME, SQL_PORT


sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0


#creates the ssh tunnel so that mqsql database can be accessed
def create_tunnel():
    tunnel = sshtunnel.SSHTunnelForwarder(
        (SSH_HOST),
        ssh_username=SSH_USER, 
        ssh_password=SSH_PASS,
        remote_bind_address=(SQL_HOSTNAME, SQL_PORT))
    return tunnel
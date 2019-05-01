import os
import paramiko

ssh = paramiko.SSHClient() 
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
ssh.connect("bank.cs.columbia.edu", username="robin", password="password")
sftp = ssh.open_sftp()
sftp.get("/home/robin/curl/src/tool_help.c", "/home/robin/Documents/tool_help.c")
sftp.close()
ssh.close()
# --- --- ---Import (modules/packages/library)--- --- ---
import pexpect
import subprocess

# --- --- ---Defined variables for the router--- --- ---
Ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'
host_name = 'Azhar'


# --- --- ---Creating SSH session--- --- ---
session = pexpect.spawn('ssh ' + username + '@' + Ip_address,
 encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# --- --- ---If an errors when creating SSH session then display error and exit--- --- ---
if result != 0:
 print('--- Failure creating a shh session for: ', Ip_address)
 exit()

# --- --- ---Session expecting password, enter the details--- --- ---
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

# --- --- ---If an error occurs when entering password details then display error and exit--- --- ---
if result != 0:
 print('--- Failure entering the password: ', password)
 exit()

# --- --- ---Enter enable mode--- --- ---
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# --- --- ---If an error occurs trying to enter enable mode then display error and exit--- --- ---
if result != 0:
 print('--- Failure in entering enable mode ---')
 exit()

# --- --- ---Send enable password details--- --- ---
session.sendline(password_enable)
result = session.expect(['# --- --- ---', pexpect.TIMEOUT, pexpect.EOF])

# --- --- ---If an error occurs when entering enable password details then display error and exit--- --- ---
if result != 0:
 print('--- Failure entering enable mode after sending the password ---')
 exit()

# --- --- ---Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)# --- --- ---', pexpect.TIMEOUT, pexpect.EOF])

# --- --- ---If an error occurs trying to enter configuration mode then display error and exit--- --- ---
if result != 0:
 print('--- Failure entering config mode ---')
 exit()

# --- --- ---output running config and save output to local file--- --- ---


# --- --- ---Send the command to output the running configuration--- --- ---
session.sendline('show running-config')
result = session.expect(['# --- --- ---', pexpect.TIMEOUT])


# --- --- ---Save the output to a local file--- --- ---
with open('running-config.txt', 'w') as f:
    f.write(session.before)  

# --- --- --- Save the output--- --- ---


# --- --- ---output startup config and save output to local file--- --- ---

# --- --- ---Send the command to output the running configuration--- --- ---
session.sendline('show startup-config')
result = session.expect(['# --- --- ---', pexpect.TIMEOUT])


# --- --- ---Save the output to a local file--- --- ---
with open('startup-config.txt', 'w') as f:
    f.write(session.before)  # --- --- --- Save the output--- --- ---

# --- --- ---Compare the start up config to the running --- --- ---
file_path_1 = "/home/devasc/labs/prne/startup-config.txt"

file_path_2 = "/home/devasc/labs/prne/running-config.txt"

   
command = f"diff {file_path_1} {file_path_2}"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print("Files are identical.")
else:
    print("Files differ:")
    print(result.stdout)

# --- --- ---Enable sys log--- --- ---
 # --- --- ---Enable System logs to keep track of all actions--- --- ---
    command = 'echo logging on'
    result = subprocess.run(command, shell=True)

# --- --- ---changing the hostname--- --- ---


# --- --- ---Change the hostname to Azhar--- --- ---
session.sendline('hostname Azhar')
result = session.expect([r'Azhar\(config\)# --- --- ---', pexpect.TIMEOUT, pexpect.EOF])

# --- --- ---If an error occurs when trying to change hostname then display error and exit--- --- ---
if result != 0:
 print('--- Failure setting the hostname ---')

# --- --- ---Exit configuration mode--- --- ---
session.sendline('exit')

# --- --- ---Exit enable mode--- --- ---
session.sendline('exit')


# --- --- ---Display a success message when logging in--- --- ---
print('-----------------------------------------------')
print('--- Hostname: ', host_name)
print('--- Successfuly connected to: ', Ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
print('Successfully Completed Coursework Task A2')
print('----------------------------------------------')


# --- --- ---Terminate the SSH session--- --- ---
session.close()
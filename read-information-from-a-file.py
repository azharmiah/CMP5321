file = open('devices-01.txt', 'r')

name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

print('Device name: ', name)
print('IP address: ', ip_address)
print('OS type: ', os_type)
print('Username: ', username)
print('Password: ', password)
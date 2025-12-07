#example of creating a simple Socket
import socket
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get local machine name
host = socket.gethostname()
# Reserve a port for your service
port = 12345
# Bind to the port
s.bind((host, port))
# Wait for client connection
s.listen(5)
print('Server listening...')
while True:
    # Establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr)
    # Send a thank you message to the client
    c.send('Thank you for connecting'.encode())
    # Close the connection
    c.close()
#server code:
import socket
def server_program():
    # Get the hostname
    host = socket.gethostname()
    port = 5000 # Initiate port
    server_socket = socket.socket() # Get instance
    server_socket.bind((host, port)) # Bind host address and port
    server_socket.listen(2)
    print("Waiting for connections...")
    conn, address = server_socket.accept() # Accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            # If data is not received, break
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode()) # Send data to the client
    conn.close() # Close the connection
if __name__ == '__main__':
    server_program()
#client code:
import socket
def client_program():
    host = socket.gethostname() # As earlier
    port = 5000 # Socket server port number
    client_socket = socket.socket() # Instantiate
    client_socket.connect((host, port)) # Connect to the server
    message = input(" -> ") # Take input
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) # Send message
        data = client_socket.recv(1024).decode() # Receive response
        print('Received from server: ' + data) # Show in terminal
        message = input(" -> ") # Again take input
    client_socket.close() # Close the connection
if __name__ == '__main__':
    client_program()

#WORKING WITH NETWORKS PROTOCOLS
#example of Using SMTP to Send an Email:

import smtplib
sender = 'your-email@example.com'
receivers = ['info@example.com']
message = """From: From Person <your-email@example.com>
To: To Person <info@example.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")

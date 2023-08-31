import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 80

def build_message(msg_num):
    """
    Builds the message to send to the server
    :param msg_num: the number of the message type
    :type msg_num: str
    :return: the message
    :rtype: str
    """
    input_msgs={
        "2":"Enter album name: ",
        "3":"Enter song name: ",
        "4":"Enter song name: ",
        "5":"Enter song: ",
        "6":"Enter text: ",
        "7":"Enter text: "
    }
    info=""
    if msg_num in input_msgs.keys():
        info=input(input_msgs.get(msg_num))
    msg=msg_num+":"+info
    return msg

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)
    msgs={
        "1":"The albums list:\n",
        "2":"The songs in the album:\n",
        "3":"The song length:\n",
        "4":"The song lyrics:\n",
        "5":"The album with this song is:\n",
        "6":"The list of songs:\n",
        "7":"The list of songs:\n",
    } # the messages to display to the user along with the server response
    msg_num=0
    server_msg = sock.recv(1024)
    server_msg = server_msg.decode()
    print(server_msg) #print welcome message
    while msg_num != "8":
        print("1: Get Albums\n2: Get Album Songs\n3: Get Song Length\n4: Get Song Lyrics\n5: Get Song Album\n6: Search Song by Name\n7: Search Song by Lyrics\n8: Quit")
        msg_num=input("Enter Number:")
        if msg_num < '1' or msg_num > '8':
            print("Invalid. Try again\n")
            continue
        msg=build_message(msg_num)
        try:    
            sock.sendall(msg.encode())
        except:
            print("Error happened")
        server_msg = sock.recv(1024)
        server_msg = server_msg.decode()
        if msg_num != 8:
            print(msgs[msg_num]+server_msg[server_msg.find(":")+1:])

if __name__=="__main__":
    main()
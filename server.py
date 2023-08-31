import socket
import select
import data
PORT=80
ANSWER = "ANSWER:"
ERROR = "ERROR:"
WELCOME_MESSAGE = "Welcome to the Pink-Floyd Server!"
QUIT_MESSAGE = "Thank you for using the Pink-Floyd Server! Bye Bye!"

def build_response(client_msg):
    """
    Builds a response for the user
    :param client_msg: the user's request
    :type client_msg: str
    :return: the response
    :rtype: str
    """
    database = data.get_parsed_data()
    if client_msg.find("8") == -1:
        options = {
            "1": data.get_albums, 
            "2": data.get_album_songs,
            "3": data.get_song_length,
            "4": data.get_song_lyrics,
            "5": data.get_song_album,
            "6": data.search_song_by_name,
            "7": data.search_song_by_lyrics
        }
        response_type = client_msg[:client_msg.find(":")]
        if response_type != '1':  # 1 doesn't need input from the user
            info = client_msg[client_msg.find(":") + 1:]
            response = options[response_type](database, info)
            if response.find("ERROR") == -1:
                response = ANSWER + response
        else:
            response = ANSWER + options[response_type](database)
    else:
        response = ANSWER + QUIT_MESSAGE
    return response


def main():
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_sock.bind(('', PORT))
    listening_sock.listen(5)
    sockets = [listening_sock]
    while True:
        read_sockets, _, _ = select.select(sockets, [], [])
        for sock in read_sockets:
            if sock == listening_sock:
                client_soc, client_address = listening_sock.accept()
                sockets.append(client_soc)
                client_soc.sendall(WELCOME_MESSAGE.encode())
                #add a new socket
            else:
                try:
                    client_msg = sock.recv(1024)
                    client_msg = client_msg.decode()
                    server_msg = build_response(client_msg)
                    sock.sendall(server_msg.encode())
                    if server_msg.find(QUIT_MESSAGE) != -1:
                        sock.close()
                        sockets.remove(sock)
                        #close socket
                except:
                    sock.close()
                    sockets.remove(sock)
                    #remove socket closed by client
if __name__ == "__main__":
    main()

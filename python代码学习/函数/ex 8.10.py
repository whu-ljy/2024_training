def show_messages(list):
    for i in list:
        print(i)

message_list = ['hi','bye','good']
show_messages(message_list)


def send_messages(list):
    send_messages = []
    for i in list:
        print(i)
        send_messages.append(i)
    print(send_messages)
send_messages(message_list)
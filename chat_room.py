class ChatRoom:
    def __init__(self, name):
        self.name = name 
        self.users = []
        self.messages = []

    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            self.messages.append(f'{user} join the chat room.')

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            self.messages.append(f'{user} leave the chat room.')
    
    def send_message(self, user, message):
        if user in self.users:
            self.messages.append(f'{user}: {message}')

    def show_message(self):
        if self.messages:
            for i in self.messages:
                print(i)
        else:
            print('No message history.')

chatroom = ChatRoom('Hello World')

#chatroom.show_message()
chatroom.join('bingbing')
chatroom.join('ziyi')

chatroom.send_message('ziyi', 'hello')
chatroom.show_message()

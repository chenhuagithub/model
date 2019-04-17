from handlers.publish import Passpory

handlers=[
    (r"/", Passpory.IndexHandler),
    (r"/chat", Passpory.ChatHandler),
]
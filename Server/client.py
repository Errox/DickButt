from socketIO_client-2 import SocketIO, LoggingNamespace

def on_bbb_response(*args):
    print('on_bbb_response', args)

with SocketIO('188.166.28.126', 8604, LoggingNamespace) as socketIO:
    socketIO.emit('bbb', {'xxx': 'yyy'}, on_bbb_response)
    socketIO.wait_for_callbacks(seconds=1)
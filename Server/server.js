var socketio = require('socket.io');
var port = 5000;

var io = socketio.listen(port);

console.log(`IO loaded and listen's to `+port);
console.log('_____________________________');

 
io.sockets.on('connection', function (socket) {
 	console.log('we have a connection');
    socket.on('send', function (data) {
    	console.log(data);
        io.sockets.emit('message', data);
    });
});



var dgram = require('dgram');
var socket = dgram.createSocket('udp4');

var testMessage = "[hello world] pid: " + process.pid;
var multicastAddress = '239.1.2.3'
var multicastPort = 5554

socket.addMembership(multicastAddress);
socket.bind(multicastPort, '0.0.0.0');

socket.on("message", function ( data, rinfo ) {
	console.log("Message received from ", rinfo.address, " : ", data.toString());
});

setInterval(function () {
	socket.send(new Buffer(testMessage), 
			0, 
			testMessage.length, 
			multicastPort, 
			multicastAddress, 
			function (err) {
				if (err) console.log(err);
				
				console.log(testMessage);
			}
	);
}, 1000);
var dgram  = require('dgram')
const { stdin } = require('process')
var cli = require('readline')

var socket = dgram.createSocket({ type: 'udp4', reuseAddr: true })

var multicastAddress = '224.1.1.1'
var multicastPort = 3000
var name = ''

var cliIfc = cli.createInterface({
    input: process.stdin,
    output: process.stdout
})

socket.on('listening', function() {
    var addr = socket.address()
    console.log("Listening on: " + addr.address + " port: " + addr.port)
    socket.setMulticastTTL(64)
    socket.addMembership(multicastAddress)
})

cliIfc.question("name", iname =>{
    name = iname
})

cliIfc.on('line', text => {
    socket.send(Buffer.from(text, 'utf-8'), 
			0, 
			text.length, 
			multicastPort, 
			multicastAddress, 
			function (err) {
				if (err) console.log(err);
			}
	);
});

socket.on("message", function ( data, rinfo ) {
	console.log("Message received from ", rinfo.address, " port: ", rinfo.port, " message: ", data.toString());
});

socket.bind(multicastPort, '0.0.0.0');
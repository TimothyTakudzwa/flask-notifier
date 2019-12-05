//Client-side Javascript code for handling random numbers
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('newnumber', function(msg) {
        console.log("message  " + msg.message.toString());
        console.log("user  " + msg.user.toString());
        
    });
});
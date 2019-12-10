//Client-side Javascript code for handling random numbers
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    console.log(socket)
    socket.on('newnumber', function(msg) {
       console.log('New items')
        
    });
});
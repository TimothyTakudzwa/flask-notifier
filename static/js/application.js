//Client-side Javascript code for handling random numbers
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/new_offer');
    console.log(socket)
    socket.on('new_offer', function(msg) {
       console.log('New items')
        
    });
});
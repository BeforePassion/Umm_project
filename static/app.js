const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

let rooms = [];

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/chat.html');
});

io.on('connection', (socket)=>{
    socket.on('request_message', (msg) => {
        // response_message로 접속중인 모든 사용자에게 msg 를 담은 정보를 방출한다.
        io.emit('response_message', msg);

    });

    // 방참여 요청
    socket.on('req_join_room', async (msg) => {
        let roomName = 'Room_' + msg;
        if(!rooms.includes(roomName)) {
            rooms.push(roomName);
        }else{
            
        }
        socket.join(roomName);
        io.to(roomName).emit('noti_join_room', "방에 입장하였습니다.");
    });

    // 채팅방에 채팅 요청
    socket.on('req_room_message', async(msg) => {
        let userCurrentRoom = getUserCurrentRoom(socket);
        io.to(userCurrentRoom).emit('noti_room_message', msg);
    });

    socket.on('disconnect', async () => {
        console.log('user disconnected');
    });
});


// TEST CODE GOES HERE
(async function(){
})();

function getUserCurrentRoom(socket){
    let currentRoom = '';
    let socketRooms = Object.keys(socket.rooms);

    for( let i = 0 ; i < socketRooms.length; i ++ ){
        if(socketRooms[i].indexOf('Room_') !== -1){
            currentRoom = socketRooms[i];
            break;
        } 
    }
    return currentRoom;
}



http.listen(3000, () => {
    console.log('Connected at 3000');
});
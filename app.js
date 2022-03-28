const http = require("http");
const server = http.createServer();
const socketio = require("socket.io");

const io = socketio(server, {
    cors: {
        origin: "http://127.0.0.1:8000",
        methods: ["GET", "POST"],
    },
});

io.on("connection", (socket) => {
    socket.on("join", (roomId) => {
        socket.join(roomId);
        io.to(roomId).emit("join", `room id is ${roomId}`);
    });
    socket.on("sendMessage", ({ message, roomId, user }) => {
        io.to(roomId).emit("sendMessage", { message: message, user: user });
    });
});

server.listen(8000, () => console.log("listening on port 8000"));
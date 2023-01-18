const roomID = JSON.parse(document.getElementById("room-id").textContent);
    const username = JSON.parse(document.getElementById("username").textContent);
    document.querySelector('#submit').onclick = function (e) {
        const messageInputDom = document.querySelector('#input');
        const message = messageInputDom.value;
        var msgval = message.length
        if (msgval > 0) {
            ChatSocket.send(JSON.stringify({
                'message': message,
                'username': username,
                'chat_id': roomID
            }));
            messageInputDom.value = '';
        }

    };


    const ChatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/current_chat/' + roomID + '/'
    );

    ChatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data)
        console.log(data)

        document.querySelector('#chat-messages').value += (data.username + ': ' + data.message + '\n')
        scroll_down_textarea()

    }
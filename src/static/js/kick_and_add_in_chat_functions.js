function KickUserFromChat(chat_id, user_id) {

    const men_shoe_link = '/chat/current_chat/delete_user/' + chat_id + '/' + user_id + '/'
    const result = $.ajax({
        type: "GET",
        url: men_shoe_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",
        success: function (data){
            return data
        }


    });
    document.querySelector('#chat-messages').value += (result + '\n')


}


function AddUserInChat(chat_id, user_id) {

    const men_shoe_link = '/chat/current_chat/add_user/' + chat_id + '/' + user_id + '/'
    const result = $.ajax({
        type: "GET",
        url: men_shoe_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",

        success: function (data){
            return data
        }


    });
    document.querySelector('#chat-messages').value += (result + '\n')

}
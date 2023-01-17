function KickUserFromChat(chat_id, user_id) {

    var men_shoe_link = '/chat/current_chat/delete_user/' + chat_id + '/' + user_id + '/'
    $.ajax({
        type: "GET",
        url: men_shoe_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",


    });

}


function AddUserInChat(chat_id, user_id) {

    var men_shoe_link = '/chat/current_chat/add_user/' + chat_id + '/' + user_id + '/'
    $.ajax({
        type: "GET",
        url: men_shoe_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",


    });

}
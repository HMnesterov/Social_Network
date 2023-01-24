function KickUserFromChat(chat_id, user_id, username) {

    const men_shoe_link = '/chat/current_chat/delete_user/' + chat_id + '/' + user_id + '/'
    const result = $.ajax({
        type: "GET",
        url: men_shoe_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",


    });

    document.querySelector('#chat-messages').value += (`${username} has been kicked from this chat!` + '\n')
    let part = document.getElementById(`Kick_${user_id}`)
    part.style.visibility = 'hidden';


}


function AddUserInChat(chat_id, user_id, person_username) {

    const men_shoe_link = '/chat/current_chat/add_user/' + chat_id + '/' + user_id + '/'
    const result = $.ajax({
        type: "GET",
        url: men_shoe_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",

        success: function (data) {
            return data
        }


    });


    let part = document.getElementById(`Add_${user_id}`)
    part.style.visibility = 'hidden';


    document.querySelector('#chat-messages').value += (`${person_username} has been added to chat!` + '\n')
}

function redirect_to_chats_list() {
    let domain = window.location.hostname
    window.location.href = '/chat/all_chats';

}

function f() {
            document.getElementsByClassName('dropdown')[0].classList.toggle('down');
            document.getElementsByClassName('arrow')[0].classList.toggle('gone');
            if (document.getElementsByClassName('dropdown')[0].classList.contains('down')) {
                setTimeout(function () {
                    document.getElementsByClassName('dropdown')[0].style.overflow = 'visible'
                }, 500)
            } else {
                document.getElementsByClassName('dropdown')[0].style.overflow = 'hidden'
            }
        }
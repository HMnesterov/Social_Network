"use strict";

function hide_button(id) {
    let part = document.getElementById(id)
    let replaced_part = document.getElementById(`insert_${id}`)
    let new_part = 'Your request has been sent to this user!'
    replaced_part.insertAdjacentHTML('beforebegin', new_part)
    part.style.visibility = 'hidden';
}


function SendFriendshipRequest(user_id) {
    const friendship_link = `/friendship/send_friendship_req/${user_id}`

    let result = $.ajax({
        type: "GET",
        url: friendship_link,
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",
        success: function (data) {
            return data
        }
    });
    hide_button(user_id)
}



// This fucntion will be used to get status of a video
window.onload = getStatus()

function getStatus () {

    fetch(window.location.origin + '/interaction-status?' + new URLSearchParams({
        video_id: window.location.href.split('/').slice(4, 5)
    }))
    .then( response => response.json() )
    .then( data => {
        // This is main task
        console.log(data)

        let like = document.getElementById('like-count')
        let views = document.getElementById('views-count')
        let dislike = document.getElementById('dislike-count')

        like.innerHTML = data['like']
        views.innerHTML = data['views']
        dislike.innerHTML = data['dislike']
    } )
    .catch( (err) => {
        console.log(err);
    })
}

function interaction(interactionType, videoId) {

    // Send a POST request
    // const csrfToken = document.querySelector("[name='csrf-token']").content
    // fetch(window.location.origin + '/feed-interaction/', {
    //     method: 'GET',
    //     data: {
    //         'type': interactionType,
    //         'video': videoId
    //     },
    //     headers: {
    //         'Accept': 'application/json',
    //         'Content-Type': 'application/json; charset=UTF-8',
    //         // "X-CSRF-Token": csrfToken,
    //         // "X-Requested-With": "XMLHttpRequest"
    //       },
    // })
    // .then( response => response.json() )
    // .then( data => {
    //     console.log(data);

    //     // To update the count
    //     getStatus();
    // } )
    // .catch( (err) => {console.log(err)} )
    // // $.ajax()

    $.ajax(
        {
            type:"GET",
            safe: false,
            url: "/feed-interaction/",
            data:{
                     video: videoId,
                     type: interactionType
            },
            success: function( data ) 
            {
                console.log(data)
                getStatus()
            }
        })
}
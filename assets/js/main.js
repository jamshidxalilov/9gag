// $(document).on("keyup", function(e) {
//     alert(e.which)
// })

// $(".selector").on("click", function(e) {
//     alert(e.which)
// })

$(".cat-link").on("click", function(e) {
    let catid = $(this).data('id')
    let catname = $(this).find(".cat-name").html()

    let header = $("#id_content > h1").first()
        if (header.length > 0) {
            header.html(catname)
        } else {
            let h1 = $("<h1/>").addClass("text-muted mt-3").html(catname)
            $("#id_content").prepend(h1)
        }

    function set_result(result) {
        $("#id_content > h1").nextAll().remove()
        $("#id_content").append(result)

    }

    // set_result("<div>Loading...</div>")

    $.ajax({
        method: "GET",
        url: "/uz/cat-ajax/" + catid + "/",
        // data: {id: catid},
        success: function(result) {
            set_result(result)

        }

    })


    return false;
})
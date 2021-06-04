// $(document).on("keyup", function(e) {
//     alert(e.which)
// })

// $(".selector").on("click", function(e) {
//     alert(e.which)
// })

$(".cat-link").on("click", function(e) {
    let catid = $(this).data('id')
    let catname = $(this).find(".cat-name").html()

    if (!confirm(gettext("Ajaxni qo'llasam bo'ladimi?"))) {
        return true
    }

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

        $("#id_content .pagination a.page-link").on("click", function(e){
            let a_href = $(this).attr("href")
            let params = new URLSearchParams(a_href)
            let page = params.get("page") || 1

            make_query(page)

            return false
        })
    }

    // set_result("<div>Loading...</div>")

    function make_query(page=1){
        set_result("<img src='/static/img/mario-running.gif' alt='loading...'/>")

        // let lang = window.location.href.split("/")[3]

        $.ajax({
            method: "GET",
            url: "/" + VAR_LANG + "/cat-ajax/" + catid + "/",
            data: {page: page},
            success: function(result) {
                set_result(result)

            }

        })
    }

    make_query()
    return false;
})

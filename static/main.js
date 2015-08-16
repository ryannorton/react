
(function poll(){
    setTimeout(function(){
        $.ajax({
            url: "/stats/",
            success: function(data){
                $("#player1").text(data)
                poll();
            },
            dataType: "text"});
        }, 200);
    }
)();

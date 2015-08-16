function convertHex(hex,opacity){
    hex = hex.replace('#','');
    r = parseInt(hex.substring(0,2), 16);
    g = parseInt(hex.substring(2,4), 16);
    b = parseInt(hex.substring(4,6), 16);
    result = 'rgba('+r+','+g+','+b+','+opacity/100+')';
    return result;
}


(function poll(){
    setTimeout(function(){
        $.ajax({
            url: "/stats/",
            success: function(data){
                console.log(data)
                $("#direction").text(data.direction)
                $("#intensity").text(data.intensity)

                $("body").css({
                    "background": convertHex("#FF0000", data.intensity)
                })
                poll();
            },
            dataType: "json"});
        }, 200);
    }
)();

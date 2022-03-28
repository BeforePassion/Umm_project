
// 크롬에서 지원하는 기능을 이용함. 휠의 전체적인 기능을 막는 코드
window.addEventListener("wheel", function(e){
    e.preventDefault();
},{passive : false});

// scrollTop을 통해 js로드시 혹시라도 Yposition
var $html = $("html");
var page = 1; 
var lastPage = $(".content").length;

$html.animate({scrollTop:0},10);

// 윈도우의 휠의 기능을 사용할 때 
$(window).on("wheel", function(e){

    if($html.is(":animated")) return;

    if(e.originalEvent.deltaY > 0){
        if(page== lastPage) return;

        page++;
    }else if(e.originalEvent.deltaY < 0){
        if(page == 1) return;

        page--;
    }
    var posTop = (page-1) * $(window).height();

    $html.animate({scrollTop : posTop});

});



console.log('hello world')
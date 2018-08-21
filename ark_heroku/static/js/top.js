$(window).on('load',function(){

	// fade-in
    $(window).scroll(function (){
        $('.fade-in').each(function(){
            var POS = $(this).offset().top;  //fade-inがついている要素の位置
            var scroll = $(window).scrollTop();  //スクロール一
            var windowHeight = $(window).height();  //ウィンドウの高さ

            if (scroll > POS - windowHeight + windowHeight/8){
                $(this).css("opacity","1" );
            } else {
                $(this).css("opacity","0" );
            }
        });
    });
});

var $container = $('#container');
// 全ての画像が読み込まれてから Masonry を初期化（イニシャライズ）
$container.imagesLoaded( function() {
  $container.masonry();
});

jQuery(function($){
  $(window).load(function(){
    var $container = $('#container');　

      $container.imagesLoaded(function(){
        $container.masonry({
          itemSelector: '.item',　
          isFitWidth: true,　
          columnWidth: 270
        });
      });


      //ウインドウがリサイズされたら発動
      $(window).resize(function() {

        var w = $(window).width();
        var x = 580;
        var y = 370;
        if (w <= y) {
          $container.imagesLoaded(function(){
            $container.masonry({
              itemSelector: '.item',　
              isFitWidth: true,　
              columnWidth: 140

            });
          });
        } else if(w <= x) {
          $container.imagesLoaded(function(){
            $container.masonry({
              itemSelector: '.item',　
              isFitWidth: true,　
              columnWidth: 170
            });
          });
        } else{
          $container.imagesLoaded(function(){
            $container.masonry({
              itemSelector: '.item',　
              isFitWidth: true,　
              columnWidth: 270
            });
          });
        }
      });

  });
});

sliderJQuery = jQuery.noConflict();
sliderJQuery(function( $ ) {
    $.global = new Object();
    $.global.total = 0;

    $(document).ready(function () {
        var slideWindowWidth = $('#slide-banner').width();
        var slideCount = $('#slides-list li').length;
        var totalSlidesWidth = slideCount * slideWindowWidth;

        $.global.item = 0;
        $.global.total = slideCount;

        $('.slide').css('width', slideWindowWidth + 'px');
        $('#slides-list').css('width', totalSlidesWidth + 'px');

        $('#left').click(function () {
            resetAutoSlide();
            performSlide('back');
        });

        $('#right').click(function () {
            resetAutoSlide();
            performSlide('forward');
        });

    });

    function performSlide(direction) {
        if (direction == 'back') {
            var nextSlideId = $.global.item - 1;
        }
        if (direction == 'forward') {
            var nextSlideId = $.global.item + 1;
        }

        if (nextSlideId == -1) {
            /* At first position and requesting 'back' -> Go to last item */
            moveCss($.global.total - 1);
        } else if (nextSlideId == $.global.total) {
            /* At last position and requesting 'forward' -> Go to first item */
            moveCss(0);
        } else {
            /* Move to requested item */
            moveCss(nextSlideId);
        }
    }

    function moveCss(nextSlideId) {
        var slideWindowWidth = $('#slide-banner').width();
        var slideCount = $('#slides-list li').length;                                                                                                   var totalSlidesWidth = slideCount * slideWindowWidth;	    
        var margin = slideWindowWidth * nextSlideId;

        $('#slides-list').css('transform', 'translate3d(-' + margin + 'px,0px,0px)');
        $('.slide').css('width', slideWindowWidth + 'px');
        $('#slides-list').css('width', totalSlidesWidth + 'px');

        $.global.item = nextSlideId;
    }

      var autoSlide = parseInt(6000, 10);
      var autoSlideInterval;
      function resetAutoSlide(){
        if(autoSlide) {
          if(autoSlideInterval) {
            clearInterval(autoSlideInterval);
          }
          autoSlideInterval = setInterval(function(){
            performSlide('forward');
          }, autoSlide)
        }
      }
      resetAutoSlide();

});

$(document).ready(function() {
      if ( $('.slider_sec .owl-carousel').lenght !=0) {
         $('.slider_sec .owl-carousel').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            dots:false,
            autoplay:true,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                1000:{
                    items:1
                }
            }
        });
      }
      if ( $('.testomonial_sld .owl-carousel').lenght !=0) {
         $('.testomonial_sld .owl-carousel').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            dots:false,
            autoplay:true,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                1000:{
                    items:1
                }
            }
        });
      }
      if ( $('.contact_testimonail_sld .owl-carousel').lenght !=0) {
         $('.contact_testimonail_sld .owl-carousel').owlCarousel({
            loop:true,
            margin:30,
            nav:true,
            dots:false,
            autoplay:true,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:2
                },
                1000:{
                    items:2
                }
            }
        });
      }
      if ( $('.portfolio_sec .owl-carousel').lenght !=0) {
         $('.portfolio_sec .owl-carousel').owlCarousel({
            loop:true,
            margin:20,
            nav:false,
            dots:false,
            responsive:{
                0:{
                    items:1
                },
                767:{
                    items:2
                },
                1000:{
                    items:3
                }
            }
        });
      }

      if ( $('.serve_area_items.owl-carousel').lenght !=0) {
         $('.serve_area_items.owl-carousel').owlCarousel({
            loop:true,
            margin:10,
            nav:false,
            dots:false,
            autoplay: true,
            center: true,
            responsive:{
                0:{
                    items:3
                },
                600:{
                    items:5
                },
                1000:{
                    items:9
                }
            }
        });
      }
    if ($(".single-blog-post .post-content p").length !=0) {
      $(".single-blog-post .post-content p").matchHeight({
        byrow: false
      });
    }if ($(".single-blog-post .post-content h3").length !=0) {
      $(".single-blog-post .post-content h3").matchHeight({
        byrow: false
      });
    }
    if ($(".service_itm").length !=0) {
      $(".service_itm").matchHeight({
        byrow: false
      });
    }
    if ($(".service_detail_itm").length !=0) {
      $(".service_detail_itm").matchHeight({
        byrow: false
      });
    }
    /*if ($(".testomonial_sld_item").length !=0) {
      $(".testomonial_sld_item").matchHeight({
        byrow: false
      });
    }*/
    if ($(".industry_sec_itm").length !=0) {
      $(".industry_sec_itm").matchHeight({
        byrow: false
      });
    }
    if ($(".news_head").length !=0) {
      $(".news_head").matchHeight({
        byrow: false
      });
    }
    $('.navbar-toggler').click(function(){
      $('body').addClass('open_nav');
    });
    $('.navbar_cross, .navbar-nav .nav-item .nav-link, .overlay_menu, .nav_sub_itm').click(function(){
        $('body').removeClass('open_nav');
        $('.navbar-collapse').removeClass('show');
    });
    $('.nav_pls').click(function(){
        $(this).toggleClass('isactive');
    });
    $('.nav_sub_itm').click(function(){
        $('.nav_pls').removeClass('isactive');
    });
});

  var changeSlide = 4; // mobile -1, desktop + 1
// Resize and refresh page. slider-two slideBy bug remove
var slide = changeSlide;
          if ($(window).width() < 600) {
             var slide = changeSlide;
              slide--;
          }
          else if ($(window).width() > 999) {
             var slide = changeSlide;
              slide++;
          }
          else{
           var slide = changeSlide;
          }
  $(document).ready(function() {
      $('.one').owlCarousel({
          nav: true,
          items: 1,
      })
      $('.two').owlCarousel({
          nav: true,
          margin: 15,
          mouseDrag: false,
          touchDrag: false,
          responsive: {
              0: {
                  items: changeSlide - 1,
                  slideBy: changeSlide - 1
              },
              600: {
                  items: changeSlide,
                  slideBy: changeSlide
              },
              1000: {
                  items: changeSlide + 1,
                  slideBy: changeSlide + 1
              }
          }
      })
      var owl = $('.one');
      owl.owlCarousel();
      owl.on('translated.owl.carousel', function(event) {
          $(".right").removeClass("nonr");
          $(".left").removeClass("nonl");
          if ($('.one .owl-next').is(".disabled")) {
              $(".slider .right").addClass("nonr");
          }
          if ($('.one .owl-prev').is(".disabled")) {
              $(".slider .left").addClass("nonl");
          }
          $('.slider-two .item').removeClass("active");
          var c = $(".slider .owl-item.active").index();
          $('.slider-two .item').eq(c).addClass("active");
          var d = Math.ceil((c + 1) / (slide)) - 1;
          $(".slider-two .owl-dots .owl-dot").eq(d).trigger('click');
      })
      $('.right').click(function() {
          $(".slider .owl-next").trigger('click');
      });
      $('.left').click(function() {
          $(".slider .owl-prev").trigger('click');
      });
      $('.slider-two .item').click(function() {
          var b = $(".item").index(this);
          $(".slider .owl-dots .owl-dot").eq(b).trigger('click');
          $(".slider-two .item").removeClass("active");
          $(this).addClass("active");
      });
      var owl2 = $('.two');
      owl2.owlCarousel();
      owl2.on('translated.owl.carousel', function(event) {
          $(".right-t").removeClass("nonr-t");
          $(".left-t").removeClass("nonl-t");
          if ($('.two .owl-next').is(".disabled")) {
              $(".slider-two .right-t").addClass("nonr-t");
          }
          if ($('.two .owl-prev').is(".disabled")) {
              $(".slider-two .left-t").addClass("nonl-t");
          }
      })
      $('.right-t').click(function() {
          $(".slider-two .owl-next").trigger('click');
      });
      $('.left-t').click(function() {
          $(".slider-two .owl-prev").trigger('click');
      });
  });

  window.onscroll = () => {
  const header = document.querySelector('.header_sec');
  if(this.scrollY <= 20) header.className = 'header_sec'; else header.className = 'header_sec scroll';
};


// number count for stats, using jQuery animate

$('.counting').each(function() {
  var $this = $(this),
      countTo = $this.attr('data-count');
  
  $({ countNum: $this.text()}).animate({
    countNum: countTo
  },

  {

    duration: 3000,
    easing:'linear',
    step: function() {
      $this.text(Math.floor(this.countNum));
    },
    complete: function() {
      $this.text(this.countNum);
      //alert('finished');
    }

  });  
  

});
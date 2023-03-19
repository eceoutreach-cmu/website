function animate(setProp, initialVal, changeInVal, duration) {
  var initialTs = new Date().getTime();
  var draw = function() {
    var progress = (Date.now() - initialTs) / duration;
    if (progress >= 1) {
      window.cancelAnimationFrame(handle);
      setProp(initialVal + changeInVal);
    }
    else {
      var easing = Math.pow(progress - 1, 3) + 1;
      setProp(initialVal + changeInVal * easing);
      var handle = window.requestAnimationFrame(draw);
    }
  }
  draw();
}

function lazyLoadImgs(callback) {
  var lazyImgs = document.querySelectorAll("[data-src]");
  for (var i = 0; i < lazyImgs.length; i++) {
    var src = lazyImgs[i].getAttribute("data-src");
    loadImage(lazyImgs[i], src);
  }
  callback();
}

function loadImage(placeholder, src) {
  var img = new Image();
  img.onload = function() {
    if (!! placeholder.parent) {
      placeholder.parent.replaceChild(placeholder, img);
    }
    else {
      placeholder.src = src;
    }
    animate(function(val) { placeholder.style.opacity = val; }, 0, 1, 300);
  }
  img.src = src;
}

function setupGalleryControls() {
  var containers = document.getElementsByClassName("photo-container");
  var gallery = document.getElementsByClassName("gallery")[0];
  for (var i = 0; i < containers.length; i++) {
    var nextButton = containers[i].getElementsByClassName("photo-next")[0];
    if (!! nextButton) {
      nextButton.addEventListener("click", function(e) {
        var nextScroll = e.currentTarget.parentElement.nextElementSibling.offsetTop;
        var scrollStart = gallery.scrollTop;
        var scrollDistance = nextScroll - scrollStart;
        animate(function(val) { gallery.scrollTop = Math.floor(val); }, scrollStart, scrollDistance, 500);
      });
    }

    var prevButton = containers[i].getElementsByClassName("photo-prev")[0];
    if (!! prevButton) {
      prevButton.addEventListener("click", function(e) {
        var prevScroll = e.currentTarget.parentElement.previousElementSibling.offsetTop;
        var scrollStart = gallery.scrollTop;
        var scrollDistance = prevScroll - scrollStart;
        animate(function(val) { gallery.scrollTop = Math.floor(val); }, scrollStart, scrollDistance, 500);
      });
    }
  }
}

function init() {
  lazyLoadImgs(setupGalleryControls);
}

function toggleDropdown() {
    var block = document.getElementById("Button-menu");
    block.classList.toggle("move");

    var dropdown = document.getElementById("menuList");
    dropdown.classList.toggle("show");
    
  }


  

window.onclick = function(event) {
  if (!event.target.matches('.nav-menu') && !event.target.matches('div')) {
    var dropdowns = document.getElementsByClassName("nav-menu");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
};

window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    document.getElementById("scrollBtn").style.display = "block";
  } else {
    document.getElementById("scrollBtn").style.display = "none";
  }
}

function scrollToTop() {
  const scrollToTop = window.setInterval(function() {
    const pos = window.pageYOffset;
    if (pos > 0) {
      window.scrollTo(0, pos - 20); // Измените значение 20 на желаемую скорость прокрутки
    } else {
      window.clearInterval(scrollToTop);
    }
  }, 2);
}


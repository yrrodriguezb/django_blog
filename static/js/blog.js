var openNav = (function () {
  if (this.className.indexOf("is-active") > 0){
    this.classList.remove("is-active");
    page.controls.navbarMenu.classList.remove("is-active");
    page.controls.navbarMenu.classList.remove("animated");
    page.controls.navbarMenu.classList.remove("bounceInDown");
  }
  else {
    this.classList.add("is-active");
    page.controls.navbarMenu.classList.add("is-active");
    page.controls.navbarMenu.classList.add("animated");
    page.controls.navbarMenu.classList.add("bounceInDown");
  }
});


var page = {
  controls: {
    navburger: null,
    navbarMenu: null,
  },
  referencesControls: function () {
    page.controls.navburger = document.getElementById('navbarBurger'),
    page.controls.navbarMenu = document.getElementById('navbarMenu')
  },
  referencesEvents: function () {
    page.controls.navburger.onclick = page.fn.openNav
  },
  fn: {
    openNav: openNav
  },
  load: function () {
    page.referencesControls();
    page.referencesEvents()
  }
}


window.onload = page.load
var text_animation_i = 0;
var text_animation_text = 'APNATVA SINGH RAWAT';
var text_animation_speed = 75;
// function text_animation_function(){
//   if (text_animation_i < text_animation_text.length){
//     document.getElementById("typing-animation").innerHTML += text_animation_text.charAt(text_animation_i);
//     text_animation_i++;
//     setTimeout(text_animation_function, text_animation_speed);
//   }
// }
function text_animation_function(){
  var places_to_animate = document.querySelectorAll(".typing-animation");
  for (var i = 0; i < places_to_animate.length; i++){
    if (text_animation_i < text_animation_text.length){
      places_to_animate[i].innerHTML += text_animation_text.charAt(text_animation_i);
    }
  }
  text_animation_i++;
  setTimeout(text_animation_function, text_animation_speed);
}
window.onscroll = function () { myFunction1() };
function myFunction1() {
  var navbar = document.getElementById("myNavbar");
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
      navbar.className = "w3-bar" + " w3-card" + " w3-animate-top" + " w3-white";
  } else {
      navbar.className = navbar.className.replace(" w3-card w3-animate-top w3-white", "");
  }
}
function toggleFunction() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
  } else {
      x.className = x.className.replace(" w3-show", "");
  }
}
function reveal1() {
  var reveals1 = document.querySelectorAll(".reveal1");
  for (var i = 0; i < reveals1.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals1[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals1[i].classList.add("active");
    } 
    // else {
    //   reveals1[i].classList.remove("active");
    // }
  }
}
function reveal3() {
  var reveals3 = document.querySelectorAll(".reveal3");

  for (var i = 0; i < reveals3.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals3[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals3[i].classList.add("active");
    } 
    // else {
    //   reveals3[i].classList.remove("active");
    // }
  }
}          
function reveal5() {
  var reveals = document.querySelectorAll(".reveal5");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } 
    // else {
    //   reveals[i].classList.remove("active");
    // }
  }
}
// https://alvarotrigo.com/blog/css-animations-scroll/
window.addEventListener("scroll", reveal1);
window.addEventListener("scroll", reveal3);
window.addEventListener("scroll", reveal5);
window.addEventListener("load", text_animation_function)
  
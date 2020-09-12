$(document).ready(function() {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function() {

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });

  let randomIdCreate = $("#random-id-create").text();
  let randomIdStored = sessionStorage.getItem("randomId");

  if (randomIdCreate > 0 && randomIdCreate !== randomIdStored) {
    sessionStorage.setItem("randomId", randomIdCreate.toString().trim());
  }

  $("#modal-form").submit(function(event) {
    let randomIdJoin = $("#random-id-join").val();

    if (randomIdJoin > 0) {
      sessionStorage.setItem("randomId", randomIdJoin.toString().trim());
    }
  });

  let socket = io();
  let event = randomIdStored.toString().trim();

  socket.on(event, function() {
    window.location.href = window.location.href;
  });

});

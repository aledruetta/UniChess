$(document).ready(function() {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function() {

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });

  let randomIdStored = null;
  let randomIdCreate = null;

  if ($("#random-id-create").text()) {
    randomIdCreate = $("#random-id-create").text().trim();
  }

  if (sessionStorage.getItem("randomId")) {
    randomIdStored = sessionStorage.getItem("randomId");
  }

  if (randomIdCreate && randomIdCreate !== randomIdStored) {
    sessionStorage.setItem("randomId", randomIdCreate);
  }

  $("#modal-cancel").click(function() {
    if (sessionStorage.getItem("randomId")) {
      sessionStorage.removeItem("randomId");
    }
  });

  $("#modal-form").submit(function() {
    let randomIdJoin = null;
    if ($("#random-id-join").val()) {
      randomIdJoin = $("#random-id-join").val().trim();
    }

    if (randomIdJoin) {
      sessionStorage.setItem("randomId", randomIdJoin);
    }
  });

  let socket = io();
  let event_name = null;
  if (randomIdStored) {
    event_name = randomIdStored.toString();

    socket.on(event_name, function() {
      window.location.href = window.location.href;
    });
  }

});

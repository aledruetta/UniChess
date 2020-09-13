$(document).ready(() => {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(() => {

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });

  getRandomIdCreate = () => {
    if ($("#random-id-create").text()) {
      return $("#random-id-create").text().trim();
    }
    return null;
  }

  getRandomIdStorage = () => {
    if (sessionStorage.getItem("randomId")) {
      return sessionStorage.getItem("randomId").toString().trim();
    }
    return null;
  }

  setRandomIdStorage = (randomIdCreate, randomIdStorage) => {
    if (randomIdCreate && randomIdCreate !== randomIdStored) {
      sessionStorage.setItem("randomId", randomIdCreate);
    }
  }

  getRandomIdJoin = () => {
    if ($("#random-id-join").val()) {
      return $("#random-id-join").val().trim();
    }
    return null;
  }

  let randomIdStored = getRandomIdStorage();
  let randomIdCreate = getRandomIdCreate();

  setRandomIdStorage(randomIdCreate, randomIdStored);

  // Cancel event
  $("#modal-cancel").click(() => {
    if (sessionStorage.getItem("randomId")) {
      sessionStorage.removeItem("randomId");
    }
  });

  // Submit event
  $("#modal-form").submit(() => {
    let randomIdJoin = getRandomIdJoin();

    if (randomIdJoin) {
      sessionStorage.setItem("randomId", randomIdJoin);
    }
  });

  // SocketIO event
  let socket = io();

  socket.on(randomIdStored, () => {
    window.location.href = window.location.href;
  });

});

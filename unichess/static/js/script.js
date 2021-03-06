$(document).ready(() => {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(() => {

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });

  getIdCreateHtml = () => {
    if ($("#random-id-create").text()) {
      return $("#random-id-create").text().trim();
    }
    return null;
  }

  getIdJoinHtml = () => {
    if ($("#random-id-join").val()) {
      return $("#random-id-join").val().trim();
    }
    return null;
  }

  getColorHtml = () => {
    if ($("#user-color").text()) {
      return $("#user-color").text().trim();
    }
    return null;
  }

  getIdStored = () => {
    if (sessionStorage.getItem("id"))
      return sessionStorage.getItem("id").toString().trim();
    return null;
  }

  setIdStored = (id) => {
    if (id && id !== getIdStored())
      sessionStorage.setItem("id", id);
  }

  getColorStored = () => {
    if (sessionStorage.getItem("color"))
      return sessionStorage.getItem("color").toString().trim();
    return null;
  }

  setColorStored = (color) => {
    if (color && color !== getColorStored())
      sessionStorage.setItem("color", color);
  }

  pathname = window.location.pathname;

  if (pathname.includes("/board/")) {
    setColorStored(getColorHtml());
    setIdStored(getIdCreateHtml());
  }
  else {
    sessionStorage.removeItem("id");
    sessionStorage.removeItem("color");
  }

  // Form cancel event
  $("#modal-cancel").click(() => {
    if (getIdStored("id"))
      sessionStorage.removeItem("id");
  });

  // Join submit event
  $("#modal-form").submit(() => {
    setIdStored(getIdJoinHtml());
  });

  // SocketIO event
  let socket = io();

  event = getIdStored() + "_" + getColorStored();
  socket.on(event, () => {
    window.location.href = window.location.href;
  });

});

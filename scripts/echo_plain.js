;(function () {
  'use strict';

  var origin = 'http://localhost:3000';

  window.addEventListener('message', function (event) {
    if (event.origin === origin) {
      event.source.postMessage('echo', origin);
    } else {
      console.error('Origin mismatch, security issue has been detected');
    }
  });

  window.top.postMessage('loaded', origin);
}());

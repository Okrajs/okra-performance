;(function () {
  'use strict';

  Perf.setViewElement(document.querySelector('#perf_results'));

  var origin = 'http://localhost:3000';
  var iframe = document.querySelector('[name=echo]');
  var iframeWindow = iframe.contentWindow;

  var i = 0;
  var max = 10000;
  var repeatTimerName = 'One 10000 postMessage subsequent `echo`';

  var repeatGet = function (event) {
    if (i === 0) {
      Perf.start(repeatTimerName);
      window.addEventListener('message', repeatGet, false);
    } else if (!event || event.origin !== origin) {
      console.error('Security issue has been detected!');
      return;
    }

    if (i < max) {
      i += 1;
      iframeWindow.postMessage('echo', origin);
    } else {
      Perf.end(repeatTimerName);
      window.removeEventListener('message', repeatGet);
    }
  };

  Perf.start('Initial load event');
  var onLoad = function () {
    window.removeEventListener('message', onLoad);

    Perf.end('Initial load event');

    repeatGet();
  };

  window.addEventListener('message', onLoad, false);
}());

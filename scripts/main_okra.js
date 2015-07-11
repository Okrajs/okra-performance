;(function () {
  /* global Okra, Perf */
  'use strict';

  Perf.setViewElement(document.querySelector('#perf_results'));

  var echoInlet = Okra.inlet(
    'echo',
    'http://localhost:3000'
  );

  var i = 0;
  var max = 10000;
  var repeatTimerName = 'One 10000 Okra subsequent `get`';

  var repeatGet = function () {
    if (i === 0) {
      Perf.start(repeatTimerName);
    }

    if (i < max) {
      i += 1;
      echoInlet.get('echo', repeatGet);
    } else {
      Perf.end(repeatTimerName);
    }
  };

  Perf.start('Initial load event');
  echoInlet.get('echo', function (value) {
    Perf.end('Initial load event');

    repeatGet();
  });
}());

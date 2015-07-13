;(function () {
  'use strict';

  Perf.setViewElement(document.querySelector('#perf_results'));

  var max = 10000;
  var timerName = 'One 10000 subsequent function call `echo`';

  var echo = function () {
    return 'echo';
  };

  Perf.start(timerName);
  for (var i=0; i<max; i+=1) {
    echo();
  }

  Perf.end(timerName);
}());

;(function () {
  /* global Firebase */

  var timers = {};
  var viewElement;
  var results = new Firebase('https://okra-perf.firebaseio.com/results');

  window.Perf = {
    setViewElement: function (el) {
      viewElement = el;
    },
    start: function (name) {
      timers[name] = performance.now();
    },
    end: function (name) {
      var value = performance.now() - timers[name];
      delete timers[name];

      if (viewElement) {
        viewElement.innerHTML += name + ': ' + value.toFixed(4) + 'ms' + '\n';
      }

      results.push({
        'location': document.location.toString(),
        'userAgent': navigator.userAgent,
        'name': name,
        'time': value,
        'createdAt': new Date()
      });

      return value;
    }
  };
}());

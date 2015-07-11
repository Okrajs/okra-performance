;(function () {
  /* global Okra */
  'use strict';

  Okra.provide('get', 'echo', function () {
    return 'echo';
  }).allowReferrer();

  Okra.useManualLoadEvent();
  Okra.emitLoadEvent();
}());

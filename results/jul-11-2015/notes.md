#Environment
 - **Laptop Make:** Acer Aspire 5750G
 - **Operating System:** Linux Ubuntu 14.04 64-bit
 - **Memmory:** 4.0 GB
 - **Processor:** Intel® Core™ i5-2430M CPU @ 2.40GHz × 4
 - **Grahpics:** Intel® Sandybridge Mobile

##Testing on Firefox
###Using Plain `postMessage`
 - Version: 38.0
 - The native debug console is open
 - The site is being served using BrowserSync local server
 - The Guake terminal is open
 - Cache configuration is on it's default settings
 - Test runs: 15
###Using Okra
 - Same environment above
 - Test runs: 12

##Testing on Chrome
###Using Plain `postMessage`
 - **Note:** The first result has been ignored because it doesn't match the
   environment bellow.
 - Version: 43.0.2357.130
 - The native devtools is open
 - The site is being served using BrowserSync local server
 - The Guake terminal is open
 - Cache is turned on
 - Test runs: 25
###Using Okra
  - Same environment above
  - Test runs: 26

###Chrome Results
    10000-echo in chrome:
    	t-test = 85.6181 pvalue = 0.0000
    	diff = 2353.3353 (okra) - 1202.9594 (plain) = 0.9563


    load in chrome:
    	t-test = 1.7282 pvalue = 0.0907
    	diff = 149.6862 (okra) - 116.5328 (plain) = 0.2845


    10000-echo in firefox:
    	t-test = -6.1051 pvalue = 0.0000
    	diff = 2424.0796 (okra) - 3190.9298 (plain) = -0.2403


    load in firefox:
    	t-test = 5.2136 pvalue = 0.0000
    	diff = 83.4338 (okra) - 31.1530 (plain) = 1.6782

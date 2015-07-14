#Environment
 - **Laptop Make:** Acer Aspire 5750G
 - **Operating System:** Linux Ubuntu 14.04 64-bit
 - **Memmory:** 4.0 GB
 - **Processor:** Intel® Core™ i5-2430M CPU @ 2.40GHz × 4
 - **Grahpics:** Intel® Sandybridge Mobile

##Testing on Chrome
###Using Plain `postMessage`
 - **Note:** The first result has been ignored because it doesn't match the
   environment bellow.
 - Version: 43.0.2357.130
 - The native devtools is open
 - The site is being served using BrowserSync local server
 - The atom is open
 - Cache is turned on
 - Test runs: 26
###Using JavaScript Native Functions
  - Same environment above
  - Test runs: 25

###Chrome Results
    10000-echo in chrome:
    	t-test = -106.1361 pvalue = 0.0000
    	diff = 1225.2338 (plain) / 0.2639 (native) = 4641.3899

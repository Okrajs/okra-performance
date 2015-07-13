#!/usr/bin/python
import json
from pprint import pprint
from sys import argv
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

try:
    json_filename = argv[1]
except IndexError:
    print 'Please proivde a json file as arugment.'
    raise

try:
    data = json.load(open(json_filename))
except:
    print 'Please provide a valid json file.'
    raise


class Stats(object):
    def __init__(self, data, browser, test_id, title = ''):
        self.browser = browser
        self.test_id = test_id
        self.data = data
        self.title = title

    def map_time(self, x):
        return x['timeMs']

    def filter_both(self, x):
        if x['browser'].startswith(self.browser):
            if x['id'] == self.test_id:
                return True

        return False

    def filter_okra(self, x):
        if x['type'] == 'okra':
            return self.filter_both(x)

        return False

    def filter_plain(self, x):
        if x['type'] == 'plain':
            return self.filter_both(x)

        return False

    def get_sets(self):
        plain = map(self.map_time, filter(self.filter_plain, self.data))
        okra = map(self.map_time, filter(self.filter_okra, self.data))

        return plain, okra

    def ttest(self):
        plain, okra = self.get_sets()

        tvalue, pvalue = ttest_ind(okra, plain, equal_var=False)
        print '%(test_id)s in %(browser)s:' % {
            "test_id": self.test_id,
            "browser": self.browser,
        }

        print '\tt-test = %(tvalue)6.4f pvalue = %(pvalue)6.4f' % {
            "tvalue": tvalue,
            "pvalue": pvalue,
        }

        print '\tdiff = %6.4f (okra) - %6.4f (plain) = %6.4f' % self.diff()

        print '\n'

    def diff(self):
        plain, okra = self.get_sets()

        okra_avg = np.average(okra)
        plain_avg = np.average(plain)

        avg_increase = okra_avg / plain_avg

        avg_increase -= 1
        return okra_avg, plain_avg, avg_increase

    def plot(self):
        plain, okra = self.get_sets()

        plt.plot(okra, 'r')
        plt.plot(plain, 'b')
        plt.xlabel('Frequency')
        plt.ylabel('Time in Milliseconds')

        if self.title:
            plt.title(self.title)

        plt.show()


echo10k_chrome = Stats(
    data=data,
    browser='chrome',
    test_id='10000-echo',
    title=(
        'Time to exchange 10,000 messages in Chrome\n'
        'using Okra (red) and plain postMessage (blue)'
    ),
)

echo10k_chrome.ttest()
echo10k_chrome.plot()


load_chrome = Stats(
    data=data,
    browser='chrome',
    test_id='load',
    title=(
        'Time to get the first `childLoad` event in Chrome\n'
        'using Okra (red) and plain postMessage (blue)'
    ),
)

load_chrome.ttest()
load_chrome.plot()


echo10k_firefox = Stats(
    data=data,
    browser='firefox',
    test_id='10000-echo',
    title=(
        'Time to exchange 10,000 messages in Firefox\n'
        'using Okra (red) and plain postMessage (blue)'
    ),
)

echo10k_firefox.ttest()
echo10k_firefox.plot()


load_firefox = Stats(
    data=data,
    browser='firefox',
    test_id='load',
    title=(
        'Time to get the first `childLoad` event in Firefox\n'
        'using Okra (red) and plain postMessage (blue)'
    ),
)

load_firefox.ttest()
load_firefox.plot()

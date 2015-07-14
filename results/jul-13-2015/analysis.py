#!/usr/bin/python
from os import path
import json
from pprint import pprint
from sys import argv
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

my_dir = path.dirname(path.realpath(__file__))
json_filename = path.join(my_dir, 'clean.json')

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

    def filter_native(self, x):
        if x['type'] == 'native':
            return self.filter_both(x)

        return False

    def filter_plain(self, x):
        if x['type'] == 'plain':
            return self.filter_both(x)

        return False

    def get_sets(self):
        plain = map(self.map_time, filter(self.filter_plain, self.data))
        native = map(self.map_time, filter(self.filter_native, self.data))

        return plain, native

    def ttest(self):
        plain, native = self.get_sets()

        tvalue, pvalue = ttest_ind(native, plain, equal_var=False)
        print '%(test_id)s in %(browser)s:' % {
            "test_id": self.test_id,
            "browser": self.browser,
        }

        print '\tt-test = %(tvalue)6.4f pvalue = %(pvalue)6.4f' % {
            "tvalue": tvalue,
            "pvalue": pvalue,
        }

        print '\tdiff = %6.4f (plain) / %6.4f (native) = %6.4f' % self.diff()

        print '\n'

    def diff(self):
        plain, native = self.get_sets()

        native_avg = np.average(native)
        plain_avg = np.average(plain)

        avg_increase = plain_avg / native_avg

        avg_increase -= 1
        return plain_avg, native_avg, avg_increase

    def plot(self):
        plain, native = self.get_sets()

        native_plot = plt.plot(native, 'ro')
        plain_plot = plt.plot(plain, 'b')

        plt.legend({
            "Native functions": native_plot,
            "postMessage": plain_plot,
        })

        plt.xlabel('Frequency')
        plt.ylabel('Time in Milliseconds')

        if self.title:
            plt.title(self.title)

        plt.show()
        plt.savefig('{my_dir}/{browser}-{test_id}.png'.format(
            my_dir=my_dir,
            browser=self.browser,
            test_id=self.test_id,
        ))


echo10k_chrome = Stats(
    data=data,
    browser='chrome',
    test_id='10000-echo',
    title='Time to exchange 10,000 messages in Chrome',
)

echo10k_chrome.ttest()
echo10k_chrome.plot()

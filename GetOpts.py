#!/usr/bin/python
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

import getopt
import sys
import re

class GetOpts(object):

    def __init__(self, args_found_callback=None, no_args_found_callback=None):
        if no_args_found_callback is None:
            self.error_callback = lambda x: x
        else:
            self.error_callback = no_args_found_callback

        if args_found_callback is None:
            self.success_callback = lambda x: x
        else:
            self.success_callback = args_found_callback

        pass

    def define_options(self, options={}):
        str_vals = ''
        str_lits = []
        key_list = []
        for key, string_val in options.iteritems():
            str_vals += str(key)
            str_lits.append(string_val)
            key_list.append([key.replace(':', ''), string_val, string_val.replace('=', ''), key])

        opts, args = getopt.getopt(sys.argv[1:], str_vals, str_lits)

        if len(opts) == 0:
            self.error_callback()

        key_val_list = {}
        for opt, arg in opts:
            o = opt.replace('-', '')
            for key in key_list:
                if key[0] == o or key[2] == o:
                    if re.search(":", key[3]) is None:
                        key_val_list[key[2]] = True
                    else:
                        key_val_list[key[2]] = arg

        for key in key_list:
            if key[2] not in key_val_list:
                if re.search(":", key[3]) is None:
                    key_val_list[key[2]] = False
                else:
                    key_val_list[key[2]] = None

        return self.success_callback(key_val_list)


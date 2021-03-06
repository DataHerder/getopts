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

    @staticmethod
    def __get_options(options={}, success_callback=None, error_callback=None):
        str_vals = ''
        str_lits = []
        key_list = []
        for key, string_val in options.iteritems():
            str_vals += str(key)
            str_lits.append(string_val)
            key_list.append([key.replace(':', ''), string_val, string_val.replace('=', ''), key])


        if '?' in sys.argv:
            pp('Allowed types: ')
            for j in key_list:
                pp('-' + j[0] + ' = ' + '--' + j[2])
            exit()

        opts, args = getopt.getopt(sys.argv[1:], str_vals, str_lits)

        if len(opts) == 0:
            error_callback([opts, args])

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

        return success_callback(key_val_list)


    def define_options(self, options={}):
        return self.__get_options(
            options=options,
            success_callback=self.success_callback,
            error_callback=self.error_callback
        )

    @classmethod
    def options(cls, options={}, success_callback=None, error_callback=None):
        if error_callback is None:
            error_callback = lambda x: x
        if success_callback is None:
            success_callback = lambda x: x

        return cls.__get_options(
            options=options,
            success_callback=success_callback,
            error_callback=error_callback
        )
#!/usr/bin/python3
import sys, toplevel

print('Module toplevel:')
toplevel.print_toplevel_status(toplevel)

print('Current module:')
toplevel.print_toplevel_status(sys.modules[__name__])

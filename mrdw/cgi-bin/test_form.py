#! /usr/bin/python3

#import cgitb
#cgitb.enable()

import yate

print(yate.start_response('text/html'))
print(yate.do_form('add_timing_data.py', ['TimeValue'], text="Send"))
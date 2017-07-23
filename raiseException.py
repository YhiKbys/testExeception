# -*- coding: utf-8 -*-
import json
import types

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    
    
    if not "key1" in event:
        raise Exception("Parameter error. Missing field 'key1'.")
    if not "key2" in event:
        raise Exception("Parameter error. Missing field 'key2'.")
    if not type(event["key1"]) is types.UnicodeType:
         raise Exception("Parameter error. 'key1' is not a UnicodeType")
         
    try:    
        # key2が整数ではない場合、例外throw
        return 10 + event["key2"]

    except Exception as e:
        raise Exception("Internal error. " + e.message)
        

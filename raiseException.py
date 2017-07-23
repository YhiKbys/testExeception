# -*- coding: utf-8 -*-
import json

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    
    
    if not "key1" in event:
        raise Exception("Parameter error. Missing field 'key1'.")
    if not "key2" in event:
        raise Exception("Parameter error. Missing field 'key2'.")
         
    try:    
        # key2が整数ではない場合、例外throw
        return 10 + event["key2"]

    except Exception as e:
        raise Exception("Internal error. " + e.message)
        

if __name__ == "__main__":
    event = {"key1" : "aaa", "key2": 1000}
    context = ""
    print(event)

    lambda_handler(event, context)

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:11:04 2020

@author: Kshitiz Regmi
"""
import re

class clean_data:
    def __init__(self):  
        pass
        
    def get_value(self,message):
        # Clean message 
        self.message =  ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", message).split())
        return self.message
        

        




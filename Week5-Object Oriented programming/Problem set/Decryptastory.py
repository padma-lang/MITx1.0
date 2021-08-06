# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:37:20 2021

@author: SRI
"""

def decrypt_story():
    joke_code = CiphertextMessage(get_story_string())
    return joke_code.decrypt_message()
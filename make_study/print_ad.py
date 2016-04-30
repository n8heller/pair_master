# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:02:55 2016

@author: n8heller
"""


def Make_Ad(study_name):
    
    ad_f = open(study_name + "_ad.html","w")
    ad_const_f = open('pair_vars/ad_const.txt','r')    

    for line in ad_const_f:
        ad_f.write(line)    
    
    ad_f.close()
    ad_const_f.close()
    return
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:07:10 2016

@author: n8heller
"""

def Make_Study(study_type, study_name, img_file_name, num_trials, num_blocks):
    
    
    # make exp.html
    if study_type == 'pair':
        Make_Pair_Exp(study_name, num_trials, num_blocks)
        
    if study_type == 'trip':
        Make_Trip_Study(study_name)
        
        
    # make ad.html
    Make_Ad(study_name)
    
        
    # make list of images  
    
    
    # set dependencies 
    Set_Dependencies(study_type, study_name, img_file_name)
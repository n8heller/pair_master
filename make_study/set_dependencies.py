# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:26 2016

@author: n8heller
"""

import shutil

def Set_Dependencies(study_type, study_name, img_file_name):
    
    if study_type == 'pair':
        master = '/home/n8heller/Desktop/simi_master/make_study/simi_pair-master'
        
    if study_type == 'trip':
        master = '/home/n8heller/Desktop/simi_master/make_study/simi_trip-master'
    
    studies = '/home/n8heller/Desktop/simi_master/Studies/'
    shutil.copytree(master, studies + study_name)


    cur_img = '/home/n8heller/Desktop/simi_master/make_study/' + img_file_name
    img = studies + study_name + '/static/images'
    shutil.copytree(cur_img, img)  


    cur_exp = '/home/n8heller/Desktop/simi_master/make_study/'+ study_name + '_exp.html'
    exp = studies + study_name + '/templates/exp.html'
    shutil.copy(cur_exp, exp)
    
    
    cur_ad = '/home/n8heller/Desktop/simi_master/make_study/'+ study_name + '_ad.html'
    ad = studies + study_name + '/templates/ad.html'
    shutil.copy(cur_ad, ad)
    
    
    
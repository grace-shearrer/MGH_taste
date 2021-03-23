#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:46:43 2018
Updated on Fri Mar 19 15:03 2021
@author: gracer
"""

#!/usr/bin/python
#get onsets


import numpy
import os
import glob

handles=[]
basepath='/Users/gracer/Documents/Output'
os.chdir(basepath)


ignore = ['Subject: '	'1234'
'18-Apr-2016 17:31:14'
'taste'	'version:1/30/16'
''
'ordernum	type	picon	beginpump	Taste_onset	picoff	swallow	rinse_onset	swallowRinseTime	endtrial'
]

#files = [file for file in os.listdir(".") if (file.lower().endswith('.log'))]
#files.sort(key=os.path.getmtime)

for file in glob.glob(os.path.join(basepath,'*.log')):
    print(file)
#if you need to get the subject number and all that see other uncomment below
#    sub=file.split('/')[5].split('_')[0]
#    session=file.split('/')[5].split('_')[2]
#    run=file.split('/')[5].split('_')[1]
#    print([sub,session,run])
#
    with open(file,'r') as infile:
        #all potential combinations
        cue_onsets=[]
        taste1_onset=[]
        taste0_onset=[]

        cues1_onset=[]
        cues0_onset=[]
        rinse=[]

        for x in infile.readlines():
#            if x.find('Keypress: q'):
#                continue

            if not x.find(ignore[0])>-1 or x.find(ignore[1])>-1:

                l_s=x.strip().split()
                print l_s
                if l_s[1] == '0':
                    cues0_onset.append(l_s[2])#when the pic is shown
                    taste0_onset.append(l_s[4])
                if l_s[1] == '1':
                    cues1_onset.append(l_s[2])#when the pic is shown
                    taste1_onset.append(l_s[4])
                rinse.append(l_s[6])

#use these names below
        r_onsets=(numpy.asarray(rinse,dtype=float))
        taste1_onsets=(numpy.asarray(taste1_onset,dtype=float))
        taste0_onsets=(numpy.asarray(taste0_onset,dtype=float))
        cue0_onsets=(numpy.asarray(cue1_onset,dtype=float))
        cue1_onsets=(numpy.asarray(cue0_onset,dtype=float))

#write new files with fancy names
#        files2make=['rinse','taste1','taste0','cue0','cue1']
#        mydict={}
#        try:
#            for files in files2make:
#                path='/Users/gracer/Desktop/Output/test/%s_%s_%s_%s.txt'%(sub,session,files,run)
#                if os.path.exists(path) == True:
#                    print ('exists')
#                    break
#                else:
                    mydict[files] = path
            #write the 3 column file, the middle number is the duration! change to the names above
            f_rinse=open(mydict['rinse'], 'w')
            for t in range(len(r_onsets)):
                f_rinse.write('%f\t3\t1\n'%(r_onsets[t]))
            f_rinse.close()

            f_TT=open(mydict['TT'], 'w')
            for t in range(len(TT_onsets)):
                f_TT.write('%f\t6\t1\n' %(TT_onsets[t]))
            f_TT.close()

            f_Tcue=open(mydict['Tcue'], 'w')
            for t in range(len(Tcue_onsets)):
                f_Tcue.write('%f\t1\t1\n' %(Tcue_onsets[t]))
            f_Tcue.close()

            f_UU=open(mydict['UU'], 'w')
            for t in range(len(UU_onsets)):
                f_UU.write('%f\t6\t1\n' %UU_onsets[t])
            f_UU.close()


        except KeyError:
            pass

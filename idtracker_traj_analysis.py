import os
import pathlib
from pprint import pprint

import numpy as np
from scipy import stats
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
# trajectorytools needs to be installed. To install, 
# pip install trajectorytools or follow the instructions at
# http://www.github.com/fjhheras/trajectorytools
import trajectorytools as tt
import trajectorytools.plot as ttplot
import trajectorytools.socialcontext as ttsocial
from trajectorytools.constants import dir_of_data

#https://gitlab.com/polavieja_lab/idtrackerai_notebooks/-/blob/master/trajectories_analysis/T0_loading_idtrackerai_trajectories.ipynb

trajectories_file_path = '/data/Sandipan_Backup/Data/Tracking2F/Videos/session_test/trajectories_wo_gaps/trajectories_wo_gaps.npy'

trajectories_dict = np.load(trajectories_file_path, allow_pickle=True).item()

def new_func(trajectories_file_path, trajectories_dict):
    print('Content of the dictionary: {}'.format(list(trajectories_dict.keys())))
    trajectories = trajectories_dict['trajectories']
    print("Loading trajectories from: ", trajectories_file_path)
    tr = tt.Trajectories.from_idtrackerai(trajectories_file_path)
    #Trajectories
    fig, ax_trajectories = plt.subplots(figsize=(5,5))
    time_range= (0, 40)
    # SET HERE THE RANGE IN SECONDS FOR WHICH YOU WANT TO PLOT THE POSITIONS
    frame_range = range(time_range[0]*tr.params['frame_rate'], time_range[1]*tr.params['frame_rate'],1)
    for i in range(tr.number_of_individuals):
    #for i in range(899):
    #print(tr.s[frame_range,i,0], tr.s[frame_range,i,1])
        ax_trajectories.plot(tr.s[frame_range,i,0], tr.s[frame_range,i,1])
        ax_trajectories.set_aspect('equal','box')
        ax_trajectories.set_title('Trajectories',fontsize=24)
        ax_trajectories.set_xlabel('X (BL)',fontsize=24)
        ax_trajectories.set_ylabel('Y (BL)',fontsize=24)

#new_func(trajectories_file_path, trajectories_dict)

def get_trajectories(num):
    trajectories = trajectories_dict['trajectories']
    tr = tt.Trajectories.from_idtrackerai(trajectories_file_path)
    time_range= (0, 40)
    frame_range = range(time_range[0]*tr.params['frame_rate'], time_range[1]*tr.params['frame_rate'],1)
    pts = tr.s[frame_range,num]
    return pts.astype(int)

pts= get_trajectories(0)





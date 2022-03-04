import pandas as pd
import torch
import idtracker_traj_analysis as trajectory_data




def loc_dataframe():
    tracks = 2
    id_list = []
    frame_list = []
    x_list = []
    y_list = []
    for track in range(tracks):    
        pts = trajectory_data.get_trajectories(track)
        frame = 1
        id = track+1
        cam = 0
        for pt in pts:
            frame_list.append(frame)
            id_list.append(id)
            x_list.append(pt[0])
            y_list.append(pt[1])
            frame = frame+1
    df = pd.DataFrame({
                'frame': frame_list, 
                'id': id_list,  
                'camT_x': x_list,
                'camT_y': y_list,
                })
    #for only top data of train 3 
    df['id']=df['id'].replace({1:2,2:1})

    df = df.sort_values(by=['frame', 'id'], ascending=[True,True])
    return df

def target_dataframe():
    gt_csv = '/data/Sandipan_Backup/Data/ZEF Dataset/3DZeF20/train/ZebraFish-03/gt/gt.txt'
    gt_df = pd.read_csv(gt_csv, sep=",", header=None, usecols=[0,1,5,6], names=['frame','id','camT_x','camT_y'])
    gt_df = gt_df.iloc[0:1600,:] #for current test
    gt_df = gt_df.sort_values(by=['frame', 'id'], ascending=[True,True])
    return gt_df

#pts = pts.reshape((-1, 1, 2))
#print(len(trajectory_data.get_trajectories))

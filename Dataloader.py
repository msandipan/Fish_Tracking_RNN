import torch
from torch.utils.data import Dataset
import pandas as pd
import DataPrep as dp




class SequenceDataset(Dataset):
    def __init__(self, sequence_length=5):
        loc_dataframe = dp.loc_dataframe()
        target_dataframe = dp.target_dataframe()
        
        self.sequence_length = sequence_length

        self.pts = list(zip(loc_dataframe.id,loc_dataframe.camT_x, loc_dataframe.camT_y))
        

        self.pts_t = list(zip(target_dataframe.camT_x, target_dataframe.camT_y))
        

    def __len__(self):
        return self.pts_l.shape[0]

    def __getitem__(self, i): 

        if i >= self.sequence_length - 1:
            i_start = i - self.sequence_length + 1
            id = self.pts[i_start][0]
            count = 0
            x=[]
            y=[]
            idx = i_start
            #print(i_start-(i + 1))
            while count<((i + 1) -i_start):
              if self.pts[idx][0] == id:
                x.append(self.pts[idx][1:3])
                y.append(self.pts_t[idx])
                count=count+1
              idx = idx+1
            x = torch.tensor(x)
            y = torch.tensor(y)
        else:
            
            id = self.pts[i][0]
            count = 0
            x=[]
            y=[]
            idx = i
            while count<((i + 1) - 0):
              if self.pts[idx][0] == id:
                x.append(self.pts[idx][1:3])
                y.append(self.pts_t[idx])
                count=count+1
              idx = idx+1
            x = torch.tensor(x)
            y = torch.tensor(y)
            padding_x = x[0].repeat(self.sequence_length - i - 1, 1)
            x = torch.cat((padding_x, x), 0)
            padding_y = y[0].repeat(self.sequence_length - i - 1, 1)
            y = torch.cat((padding_y, y), 0)

        return x,y
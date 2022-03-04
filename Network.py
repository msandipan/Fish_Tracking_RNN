import torch
import torch.nn as nn
import torch.nn.functional as F

class UnfoldingLSTM(nn.ModuleList):
    def __init__(self, args):
	    super(UnfoldingLSTM, self).__init__()
	
	    # Number of samples per time step
	    self.batch_size = 2
	
	    # Dimension of weight vectors
	    self.hidden_dim = 16
    
	    
	
	    # Number of time steps
	    self.sequence_len = 5
	
	    # Initialize embedding layer
	    #self.embedding = nn.Embedding(self.input_size, self.embedding_dim, padding_idx=0)
	
	    # Initialize LSTM Cell
	    self.lstm_cell = nn.LSTMCell(self.embedding_dim, self.hidden_dim)

    def forward(self, x):
        
	# Creation of cell state and hidden state
	    hidden_state = torch.zeros(x.size(0), self.hidden_dim)
	    cell_state = torch.zeros(x.size(0), self.hidden_dim)
	
	# Weights initialization
	    torch.nn.init.xavier_normal_(hidden_state)
	    torch.nn.init.xavier_normal_(cell_state)
	
	# From idx-token to embedded tensors
	   # out = self.embedding(x)
	
	# Prepare the shape for LSTMCell
	    out = out.view(self.sequence_len, x.size(0), -1)
	
	# Unfolding LSTM
	    for i in range(self.sequence_len):
		    hidden_state, cell_state = self.lstm_cell(out[i], (hidden_state, cell_state))
		
	    return hidden_state
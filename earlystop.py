import numpy as np

class EarlyStopper:
    def __init__(self, patience=10, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.min_training_loss = np.inf

    def early_stop(self, training_loss):
        if training_loss < self.min_training_loss:
            self.min_training_loss = training_loss
            self.counter = 0
        elif training_loss > (self.min_training_loss + self.min_delta):
            self.counter += 1
            if self.counter >= self.patience:
                print ("Early Stopping triggered, patience = "+self.patience)
                return True
        return False
    
## How to use 
# early_stopper = EarlyStopper(patience=3, min_delta=10)
# for epoch in np.arange(n_epochs):
#     train_loss = train_one_epoch(model, train_loader)
#     validation_loss = validate_one_epoch(model, validation_loader)
#     if early_stopper.early_stop(validation_loss):             
#         break
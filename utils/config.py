"""
    This file contains constants used throughout the project
    as well as a configuration class, which is used as a
    training utility.
"""
# data constants, PC-specific (!absolute paths)
tr_root = 'C:/Users/arind/Downloads/clips'
tr_subdirs = ['0601', '0531', '0313-1', '0313-2']
tr_flabels = ['C:/Users/arind/Downloads//label_data_0601.json',
               'C:/Users/arind/Downloads/label_data_0531.json',
               'C:/Users/arind/Downloads/label_data_0313.json']

ts_root = 'C:/Users/arind/Downloads/clips'
ts_subdirs = ['0601', '0531', '0313-1', '0313-2']
ts_flabels = ['C:/Users/arind/Downloads/label_data_0601.json',
               'C:/Users/arind/Downloads/label_data_0531.json',
               'C:/Users/arind/Downloads/label_data_0313.json']

data_dir = 'visual-results/'


class Configs:
    """
        Class containing hyperparameters values as well
        as various configuration used throughout the
        project.
    """
    def __init__(self):
        # hyperparameters
        self.epochs = 2
        self.init_lr = 0.001
        self.batch_size = 10
        self.test_batch = 100
        self.workers = 1
        self.momentum = 0.9
        self.weight_decay = 0.0001
        self.loss_weights = [0.02, 1.02]

        # convlstm hidden dim
        self.hidden_dims = [512, 512]
        # vgg 16 decoder config
        self.decoder_config = [512, 512, 256, 128, 64]

        self.load_model = True

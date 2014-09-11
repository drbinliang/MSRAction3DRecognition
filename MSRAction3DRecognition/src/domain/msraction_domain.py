'''
Created on 10 Sep 2014

@author: bliang03
'''
from dataset_configs import msraction_dataset_config

class MsrAction:
    """ Class for msr action """
    
    def __init__(self, fileName):
        """ Initialize Gesture using basic information """
        file_names = fileName.split('_')
        self._actionName = file_names[0]
        self._actionID = msraction_dataset_config.actionCateogory.index(self._actionName)
        self._subjectID = file_names[1]
        self._elementID = file_names[2]
        self.depthSequence = None
        
    @property
    def actionName(self):
        return self._actionName 
    
    @property
    def actionID(self):
        return self._actionID 

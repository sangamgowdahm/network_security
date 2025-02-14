import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging as logger
import os,sys
import numpy as np
#import dill
import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open (file_path,'w')as file:
            yaml.dump(content,file)

    except Exception as e:
            raise NetworkSecurityException(e,sys)          
    
def save_numpy_array_data(file_path,array:np.array):
    '''save numpy array data to file file_path :str location of file to save array:np.array data to save'''    

    try:
       dir_path=os.path.dirname(file_path)
       os.makedirs(dir_path,exist_ok=True)
       with open(file_path,'wb')as file_obj:
           np.save(file_obj,array)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    
def save_object(file_path:str,obj:object)->None:
    try:
        logger.info('entered the save_oject method of main_untils class')
        cv=os.path.dirname(file_path)
        os.makedirs(cv,exist_ok=True)
        with open(file_path,'wb')as file_obj:
            pickle.dump(obj,file_obj)
        logger.info("exited the save objects methods from mainutils class")   

    except Exception as e:
        raise NetworkSecurityException(e,sys ) from e        


def load_object(file_path:str,)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f'the file :{file_path}is not exists')
        with open(file_path,'rb')as file_obj:
            print(file_obj)
            return pickle.load(file_obj)            
    except Exception as e:
        raise NetworkSecurityException(e,sys ) from e   
    
def load_numpy_array_data(file_path:str)->np.array:
  '''
  load numpy array data from file
  file_path:str locartion of file to load
  returm:nparray data loaded
  '''    
  try:
      with open(file_path,'rb') as file_obj:
          return np.load(file_obj)
  except Exception as e:
      raise NetworkSecurityException(e,sys)from e
  
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(models)):
            model_name = list(models.keys())[i]  # Get model name
            model = models[model_name]  # Get model instance
            para = param[model_name]  # Get hyperparameter grid

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score  # Store test score

        return report  

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

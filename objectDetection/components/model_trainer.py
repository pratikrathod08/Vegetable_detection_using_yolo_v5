import os , sys
import shutil
import yaml 
import zipfile
from objectDetection.utils.main_utils import read_yaml_file
from objectDetection.logger import logging  
from objectDetection.exception import AppException
from objectDetection.entity.config_entity import ModelTrainerConfig
from objectDetection.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config : ModelTrainerConfig,
        ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method for ModelTrainer class") 

        try:
            logging.info('Unzipping data ')

            with zipfile.ZipFile("data.zip",'r') as zip_ref:
                zip_ref.extractall(os.getcwd())
            # os.system("unzip data.zip")
            # os.system("rm data.zip")
            os.remove("data.zip")

            with open('data.yaml', 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)

            with open(f'yolov5/models/custom_{model_config_file_name}.yaml','w') as f:
                yaml.dump(config , f)

            os.system(f"cd yolov5/ && python train.py --img 608 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5x.yaml --weights {self.model_trainer_config.weight_name} --name yolov5x_results --cache")
            # os.system(f"cp yolov5/runs/train/yolov5x_results/best.pt yolov5/")
            shutil.copyfile("yolov5/runs/train/yolov5x_results/best.pt" , "yolov5/best.pt")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            #os.system(f"cp yolov5/runs/trtain/yolov5x_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
            shutil.copyfile("yolov5/runs/trtain/yolov5x_results/weights/best.pt" , "{self.model_trainer_config.model_trainer_dir}/best.pt")


            # os.system("rm -rf yolov5/runs")
            # os.system("rm -rf train")
            # os.system("rm -rf valid")
            # os.system("rm -rf data.yaml")

            os.remove("README.dataset.txt")
            os.remove("README.roboflow.txt")
            os.remove("train")
            os.remove("test")
            os.remove("valid")
            os.remove("data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path="yolov5/best.pt")

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model Trainer Artifact : {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e , sys)      

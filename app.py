from objectDetection.logger import logging
from objectDetection.exception import AppException
from objectDetection.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
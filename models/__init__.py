#!/usr/bin/python3
"""models"""
from models.base_model import BaseModel
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

classes = {"BaseModel": BaseModel}
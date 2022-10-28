#!/usr/bin/python3
""" creates unique file storage instances
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

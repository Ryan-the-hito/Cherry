#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout,
                             QComboBox, QLineEdit, QProgressBar)
import sounddevice as sd
import subprocess
import numpy as np
import os
import re
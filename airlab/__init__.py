# Copyright 2018 University of Basel, Center for medical Image Analysis and Navigation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

# sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "/airlab/airlab"))
# print(sys.path)

# # os.chdir('airlab/airlab')
# cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(cwd)
# sys.path.append(os.path.join(cwd))
# # sys.path.append(os.path.join(cwd, 'airlab'))
# os.chdir(cwd)
# print(os.getcwd())
# print(sys.path)

from .utils import *
import airlab.airlab.transformation
import airlab.airlab.loss
from .registration import *
import airlab.airlab.regulariser

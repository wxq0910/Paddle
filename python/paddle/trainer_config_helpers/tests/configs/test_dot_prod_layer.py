#  Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserve.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from paddle.trainer_config_helpers import *

vec1 = data_layer(name='vector1', size=10)
vec2 = data_layer(name='vector2', size=10)
dot_product = dot_prod_layer(input1=vec1, input2=vec2)

outputs(dot_product)

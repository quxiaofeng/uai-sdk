# Copyright 2017 The UAI-SDK Authors. All Rights Reserved.
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
# ==============================================================================

from uai.api.base_api import BaseUaiServiceApiOp

class ModifyUAISrvVersionMemoApiOp(BaseUaiServiceApiOp):

    ACTION_NAME = "ModifyUAISrvVersionMemo"

    def __init__(self, public_key, private_key, service_id, srv_version, srv_version_memo, project_id='', region='', zone=''):
        super(ModifyUAISrvVersionMemoApiOp, self).__init__(self.ACTION_NAME, public_key, private_key, project_id, region, zone)
        self.cmd_params['Region'] = region if region != '' else super(ModifyUAISrvVersionMemoApiOp, self).PARAMS_DEFAULT_REGION
        self.cmd_params['ServiceID'] = service_id
        self.cmd_params['SrvVersion'] = srv_version
        self.cmd_params['SrvVerMemo'] = srv_version_memo

    def _check_args(self, params):
        if params['ServiceID'] == '':
            return False
        if params['SrvVersion'] == '':
            return False
        if params['SrvVerMemo'] == '':
            return False
        return True

    def call_api(self):
        succ, self.rsp = super(ModifyUAISrvVersionMemoApiOp, self).call_api()
        return succ, self.rsp

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.network import network_service
from openstack import resource


class QoSPolicy(resource.Resource):
    resource_key = 'policy'
    resources_key = 'policies'
    base_path = '/qos/policies'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    #: QoS policy name.
    name = resource.prop('name')
    #: The ID of the project who owns the network. Only administrative
    #: users can specify a project ID other than their own.
    project_id = resource.prop('tenant_id')
    #: The QoS policy description.
    description = resource.prop('description')
    #: Indicates whether this QoS policy is shared across all projects.
    #: *Type: bool*
    is_shared = resource.prop('shared', type=bool)
    #: List of QoS rules applied to this QoS policy.
    rules = resource.prop('rules')
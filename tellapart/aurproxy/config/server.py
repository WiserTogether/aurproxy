# Copyright 2015 TellApart, Inc.
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

import itertools
import hashlib
from tellapart.aurproxy.util import slugify

class ProxyServer(object):
  def __init__(self, hosts, ports, healthcheck_route, routes, streams, context):
    self.hosts = hosts
    self.ports = ports
    self.healthcheck_route = healthcheck_route
    self.routes = routes
    self.streams = streams
    self.context = context

  @property
  def slug(self):
    hosts_part = ''
    if self.hosts:
      hosts_part = '__'.join([slugify(h) for h in self.hosts])
    ports_part = '__'.join([slugify(p) for p in self.ports])
    s = 's__'
    if hosts_part:
      s = '{0}{1}__'.format(s, hosts_part)
    if ports_part:
      s = '{0}{1}__'.format(s, ports_part)
    return hashlib.sha256(s).hexdigest()

  @property
  def blueprints(self):
    return list(itertools.chain(*[r.blueprints for r in self.routes])) + \
           list(itertools.chain(*[s.blueprints for s in self.streams]))

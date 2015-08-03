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

class ProxyStream(object):
  def __init__(self, source_group_manager):
    """
    Represents a balanceable grouping of TCP endpoints.

    Args:
      source_group_manager - SourceGroupManager instance that manages weights
        across endpoints.
    """
    self._source_group_manager = source_group_manager

  @property
  def blueprints(self):
    """
    A collection of the flask blueprints to expose for this stream.
    """
    return self._source_group_manager.blueprints

  @property
  def endpoints(self):
    """
    A collection of endpoints managed by this stream.
    """
    return self._source_group_manager.endpoints

  @property
  def slug(self):
    """
    A configuration-file-compatible unique name for this stream.
    """
    return self._source_group_manager.slug

  def start(self, weight_adjustment_start):
    """
    Start managing this stream. Required before usage.

    Args:
      weight_adjustment_start - The time at which to start adjusting endpoint
      weights.
    """
    self._source_group_manager.start(weight_adjustment_start)

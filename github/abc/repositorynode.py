"""
/github/abc/repositorynode.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class RepositoryNode():
    """
    Represents a node which belongs to a repository.

    https://developer.github.com/v4/interface/repositorynode/
    """

    __slots__ = ()

    @property
    def repository(self) -> "Repository":
        """
        The repository the node belongs to.
        """

        return self.data["repository"]
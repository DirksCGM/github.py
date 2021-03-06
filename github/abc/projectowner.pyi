from typing import List

from github.iterator import CollectionIterator
from github.enums import ProjectTemplate
from github.objects import Project


class ProjectOwner():
    @property
    def projects_resource_path(self) -> str: ...
    @property
    def projects_url(self) -> str: ...
    @property
    def viewer_can_create_projects(self) -> bool: ...

    async def fetch_project(self, number: int) -> Project: ...
    
    def fetch_projects(self, **kwargs) -> CollectionIterator: ...

    async def create_project(self, *, name: str, body: str=..., template: ProjectTemplate=...) -> Project: ...

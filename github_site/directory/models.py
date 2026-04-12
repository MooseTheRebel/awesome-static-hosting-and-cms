from dataclasses import dataclass


@dataclass
class ContentManagementSystem:
    name: str
    source_url: str
    description: str
    tags: list[str]
    issue: str


@dataclass
class HostingProvider:
    name: str
    url: str
    description: str
    tags: list[str]
    issue: str

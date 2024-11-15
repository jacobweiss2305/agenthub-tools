#!/usr/bin/env python3
import os
import argparse
from pathlib import Path
from typing import Optional

class PackageCreator:
    def __init__(
        self,
        package_name: str,
        version: str = "0.0.1",
        description: Optional[str] = None,
        author: str = "Jacob Weiss",
        email: str = "jaweiss2305@gmail.com"
    ):
        self.package_name = package_name.lower().strip()
        self.version = version
        self.description = description
        self.author = author
        self.email = email
        
        # Set paths
        self.package_root = Path(f"packages/{self.package_name}")
        self.src_path = self.package_root / "src" / "aihive_tools" / self.package_name

    def create_directories(self):
        """Create the package directory structure."""
        directories = [
            self.package_root,
            self.package_root / "src" / "aihive_tools" / self.package_name,
            self.package_root / "tests",
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {directory}")

    def create_core_package(self):
        """Create the core package with base classes."""
        # Create base.py
        base_content = '''from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    """Base class that all AIHive tools must implement."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the tool."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what the tool does."""
        pass
    
    @abstractmethod
    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        """Execute the tool's main functionality."""
        pass
'''
        (self.src_path / "base.py").write_text(base_content)
        print("Created base.py")

        # Create __init__.py
        init_content = f'''"""AIHive core package."""

from .base import BaseTool

__version__ = "{self.version}"

__all__ = ["BaseTool"]
'''
        (self.src_path / "__init__.py").write_text(init_content)
        print("Created __init__.py")

    def create_tool_package(self):
        """Create a tool package."""
        # Create __init__.py
        init_content = f'''"""AIHive {self.package_name} integration package."""

__version__ = "{self.version}"
'''
        (self.src_path / "__init__.py").write_text(init_content)
        print("Created __init__.py")

        # Create tools.py
        tool_class_name = f"{self.package_name.capitalize()}Tool"
        tools_content = f'''from typing import Any, Dict
from aihive_tools.core import BaseTool

class {tool_class_name}(BaseTool):
    """
    {self.package_name.capitalize()} integration for AIHive.
    """
    
    name = "{self.package_name}"
    description = "{self.description or f'AIHive integration for {self.package_name}'}"
    
    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Execute the {self.package_name} tool's main functionality.
        
        Args:
            **kwargs: Tool-specific arguments
            
        Returns:
            Dict[str, Any]: Results of the operation
        """
        raise NotImplementedError("{self.package_name} tool not implemented yet")
'''
        (self.src_path / "tools.py").write_text(tools_content)
        print("Created tools.py")

    def create_pyproject_toml(self):
        """Create the pyproject.toml file."""
        dependencies = []
        if self.package_name != "core":
            dependencies.append(f'"aihive-tools-core>={self.version}"')
        
        content = f'''[project]
name = "aihive-tools-{self.package_name}"
version = "{self.version}"
description = "{self.description or f'AIHive {self.package_name} package'}"
requires-python = ">=3.7"
readme = "README.md"
authors = [
    {{ name = "{self.author}", email = "{self.email}" }}
]

dependencies = [
    {",".join(dependencies)}
]

[project.urls]
homepage = "https://github.com/jacobweiss2305/aihive-tools"
repository = "https://github.com/jacobweiss2305/aihive-tools/tree/main/packages/{self.package_name}"

[build-system]
requires = ["setuptools>=45", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {{"" = "src"}}

[tool.setuptools.packages.find]
where = ["src"]
include = ["aihive_tools.{self.package_name}*"]
'''
        (self.package_root / "pyproject.toml").write_text(content)
        print("Created pyproject.toml")

    def create_readme(self):
        """Create the README.md file."""
        if self.package_name == "core":
            content = '''# AIHive Core

Core package for the AIHive framework, providing base classes and utilities.

## Installation

```bash
pip install aihive-tools-core
```

## Usage

```python
from aihive_tools.core import BaseTool

class MyTool(BaseTool):
    name = "my-tool"
    description = "My custom tool"
    
    def execute(self, **kwargs):
        # Implement tool logic
        pass
```
'''
        else:
            content = f'''# AIHive {self.package_name.capitalize()} Tool

This package provides {self.package_name} integration for the AIHive framework.

## Installation

```bash
pip install aihive-tools-{self.package_name}
```

## Usage

```python
from aihive_tools.{self.package_name} import {self.package_name.capitalize()}Tool

tool = {self.package_name.capitalize()}Tool()
result = tool.execute()
```
'''
        (self.package_root / "README.md").write_text(content)
        print("Created README.md")

    def create_package(self):
        """Create the complete package structure."""
        if ' ' in self.package_name:
            raise ValueError("Package name cannot contain spaces")

        self.create_directories()
        
        if self.package_name == "core":
            self.create_core_package()
        else:
            self.create_tool_package()
            
        self.create_pyproject_toml()
        self.create_readme()

        print(f"\nPackage aihive-tools-{self.package_name} created successfully!")

def main():
    parser = argparse.ArgumentParser(description="Create a new AIHive package")
    parser.add_argument("package_name", help="Name of the package (e.g., 'core', 'jira')")
    parser.add_argument("--version", default="0.0.1", help="Package version")
    parser.add_argument("--description", help="Package description")
    parser.add_argument("--author", default="Jacob Weiss", help="Package author")
    parser.add_argument("--email", default="jaweiss2305@gmail.com", help="Author's email")

    args = parser.parse_args()

    creator = PackageCreator(
        package_name=args.package_name,
        version=args.version,
        description=args.description,
        author=args.author,
        email=args.email
    )
    
    creator.create_package()

if __name__ == "__main__":
    main()
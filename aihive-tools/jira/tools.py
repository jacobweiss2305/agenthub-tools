# aihive_tools/jira/tools.py
from typing import Dict, Any, Optional
import json

try:
    from jira import JIRA
except ImportError:
    raise ImportError(
        "`jira` not installed. Please install using `pip install aihive-tools-jira`"
    )

def create_jira_issue(project_key: str, summary: str, description: str, **kwargs) -> str:
    """Create a new JIRA issue.
    
    Args:
        project_key (str): The project key where the issue will be created
        summary (str): Issue summary/title
        description (str): Issue description
        **kwargs: Additional arguments for JIRA configuration and issue fields
            - server (str): JIRA server URL
            - token (str): Authentication token
            - issue_type (str): Type of issue (default: "Task")
            - additional_fields (Dict): Any additional fields for the issue
    
    Returns:
        str: JSON string containing the created issue details
    """
    # Initialize JIRA client
    jira = JIRA(
        server=kwargs.get('server'),
        token_auth=kwargs.get('token')
    )
    
    # Prepare issue dictionary
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': kwargs.get('issue_type', 'Task')},
    }
    
    # Add any additional fields
    additional_fields = kwargs.get('additional_fields', {})
    issue_dict.update(additional_fields)
    
    # Create issue and convert to dict for JSON serialization
    issue = jira.create_issue(fields=issue_dict)
    
    # Convert issue to dictionary for JSON serialization
    issue_dict = {
        'id': issue.id,
        'key': issue.key,
        'self': issue.self,
        'summary': issue.fields.summary,
        'description': issue.fields.description,
        'status': str(issue.fields.status),
        'issue_type': str(issue.fields.issuetype),
    }
    
    return json.dumps(issue_dict, indent=2)

def get_jira_issue(issue_key: str, **kwargs) -> str:
    """Get JIRA issue details.
    
    Args:
        issue_key (str): The issue key to retrieve (e.g., "PROJ-123")
        **kwargs: Additional arguments for JIRA configuration
            - server (str): JIRA server URL
            - token (str): Authentication token
            - fields (List[str]): Specific fields to retrieve
    
    Returns:
        str: JSON string containing the issue details
    """
    # Initialize JIRA client
    jira = JIRA(
        server=kwargs.get('server'),
        token_auth=kwargs.get('token')
    )
    
    # Get issue
    issue = jira.issue(
        issue_key, 
        fields=kwargs.get('fields', '*all')
    )
    
    # Convert issue to dictionary for JSON serialization
    issue_dict = {
        'id': issue.id,
        'key': issue.key,
        'self': issue.self,
        'summary': issue.fields.summary,
        'description': issue.fields.description,
        'status': str(issue.fields.status),
        'issue_type': str(issue.fields.issuetype),
        'created': str(issue.fields.created),
        'updated': str(issue.fields.updated),
        'assignee': str(issue.fields.assignee) if issue.fields.assignee else None,
        'reporter': str(issue.fields.reporter) if issue.fields.reporter else None,
    }
    
    return json.dumps(issue_dict, indent=2)
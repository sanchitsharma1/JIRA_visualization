import plotly.graph_objects as go
import numpy as np

# Sample data: Dictionary with assignees and their issues
jira_data = {
    'Assignee1': ['Issue1', 'Issue2', 'Issue3'],
    'Assignee2': ['Issue4', 'Issue5'],
    'Assignee3': ['Issue7', 'Issue8', 'Issue9'],
    'Assignee4': ['Issue10', 'Issue11', 'Issue12'],
    'Assignee5': ['Issue13', 'Issue14', 'Issue15'],
    'Assignee6': ['Issue16', 'Issue17', 'Issue18'],
    'Assignee7': ['Issue19', 'Issue20'],
    'Assignee8': ['Issue21', 'Issue22', 'Issue23'],
    'Assignee9': ['Issue24', 'Issue25', 'Issue26'],
    'Assignee10': ['Issue27', 'Issue28', 'Issue29'],
}

# Extract assignees and issues
assignees = list(jira_data.keys())
issues = list(set(issue for issues in jira_data.values() for issue in issues))

# Create a grouped bar chart
fig = go.Figure()

for i, issue in enumerate(issues):
    issue_data = [1 if issue in jira_data[assignee] else 0 for assignee in assignees]
    fig.add_trace(go.Bar(x=assignees, y=issue_data, name=f'Issue {i + 1}'))

fig.update_layout(
    barmode='stack',
    title='JIRA Issue Assignment (Grouped Bar Chart)',
    xaxis=dict(title='Assignees'),
    yaxis=dict(title='Issue Assignment'),
)

fig.show()

# 0x19-postmortem

## Issue Summary:
On the morning of 2021-09-14, there was an incident with the server that resulted in the website being down for 2 hours. The website was not accessible to users during this time. The issue was caused by the server running out of disk space.

## Timeline:
- 2021-09-14 10:00: The server went down.
- 2021-09-14 10:10: The team discovered that the server was out of disk space.
- 2021-09-14 10:15: The team identified the files that were taking up the most space.
- 2021-09-14 10:30: The team deleted unnecessary log files and temporary files to free up disk space.
- 2021-09-14 12:00: The server was back online and the website was accessible to users again.

## Root Cause:
The root cause of the issue was the server running out of disk space. This was due to the accumulation of log files and temporary files over time. The server did not have a mechanism in place to automatically clean up these files, which led to the disk space issue.

## Corrective and Preventative Measures:
To prevent this issue from happening again in the future, the following corrective and preventative measures will be implemented:
- Implement a log rotation mechanism to manage log files and prevent them from taking up too much disk space.
- Set up a scheduled job to clean up temporary files on a regular basis.
- Monitor disk space usage regularly to identify potential issues before they impact the server.
- Implement alerts to notify the team when disk space usage reaches a critical level.
- Review server configuration and optimize disk space allocation as needed.
- Conduct regular audits of disk space usage to ensure that the server has enough space to operate efficiently.

## Additional Notes:
The team responded quickly to the incident and was able to resolve the issue within 2 hours. The website is now back online and accessible to users. The team will continue to monitor the server and implement measures to prevent similar incidents in the future.
```

### 20. My first API
Write a Python script that fetches data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) and create a CSV file with all tasks for a given employee ID.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: `"USER_ID","USERNAME","TASK

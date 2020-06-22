# Agent-Selector-based-on-issue

This code is basically used for selecting agent(s) to help with issues that are registered.
When an issue comes in we need to present the issue to one or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest ,i.e, the highest time difference between the agent availability time and the issue registered time. In random mode we randomly pick an agent. An issue also has one or many roles (Sales/Support/Spanish speaker). Issues are presented to agents only with matching roles.

Here is the output for the lists that I have made:

![try1](https://user-images.githubusercontent.com/22218522/85280673-38e00e00-b4a6-11ea-97fb-e92748e9d0a0.PNG)
![try2](https://user-images.githubusercontent.com/22218522/85280677-3a113b00-b4a6-11ea-9855-0fb612ca62a5.PNG)
![try3](https://user-images.githubusercontent.com/22218522/85280680-3aa9d180-b4a6-11ea-86d5-6f8737e88cc2.PNG)
![try4](https://user-images.githubusercontent.com/22218522/85280684-3b426800-b4a6-11ea-9bc5-cb59fd05007e.PNG)


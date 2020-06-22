# Agent-Selector-based-on-issue

This code is basically used for selecting agent(s) to help with issues that are registered.
When an issue comes in we need to present the issue to one or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest ,i.e, the highest time difference between the agent availability time and the issue registered time. In random mode we randomly pick an agent. An issue also has one or many roles (Sales/Support/Spanish speaker). Issues are presented to agents only with matching roles.


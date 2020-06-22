import datetime
import random

agent_list= [1001, True, datetime.time(8, 0), 'Support', 1002, True, datetime.time(10, 0), 'Sales', 1003, True, datetime.time(11, 0), 'Spanish speaker', 1004, True, datetime.time(12, 0), 'Sales', 1005, True, datetime.time(11, 0), 'Support', 1006, True, datetime.time(12, 0), 'Spanish speaker', 1007, True, datetime.time(15, 0), 'Sales', 1008, True, datetime.time(16, 0), 'Spanish speaker', 1009, True, datetime.time(9, 0), 'Sales', 1010, True, datetime.time(16, 0), 'Support']
roles = ['Support', 'Sales', 'Spanish speaker']
""" 
LIST OF AGENTS
The following code is to enter details of agents to create an agent list. 
It also takes into consideration the types of roles by making a list of roles.

AGENT LIST CREATION (OPTIONAL)
i = 'Y'
agent_list = []
roles = []
while i == 'Y': 
    add_detail = input('Do you want to enter agent details (Y/N):')
    if add_detail == 'Y':
        agent_id = int(input('Agent ID:'))
        is_available = bool(input('Agent Availablity (True/False):'))
        available = input('specify time since agent is available in HH,MM format:')
        available = available.split(',')
        available_since = datetime.time(int(available[0]),int(available[1]))
        role = str(input('Enter the Role:'))
        agent_list.append(agent_id)  
        agent_list.append(is_available)
        agent_list.append(available_since)
        agent_list.append(role)
        if role not in roles:
            roles.append(role)
    else:
        break
"""

issues = [9001, 'Technical problems with the platform', datetime.time(13, 38), 'Support', 9002, 'Want to know about features in spanish language.', datetime.time(8, 49), 'Sales,Spanish speaker', 9003, 'Want an AI chatbot for my website', datetime.time(11, 39), 'Sales,Support', 9004, 'Want to know about features in Japanese Language', datetime.time(10, 40), 'Japanese speaker,Sales']
"""
LIST OF ISSUES
The following code is to enter the issue and the type of role/roles of agents related to the issue.

issues = []
j = 'Y'
while j == 'Y': 
    add_detail = input('Do you want to enter issues details (Y/N):')
    if add_detail == 'Y':
        issue_id = int(input('Issue ID:'))
        issue_desp = input('Issue:')
        role_issue = str(input('Enter the Roles involved separated by comma:'))
        timenow = ((datetime.datetime.now()).strftime("%X")).split(":")
        #timenow = timenow.split(":")
        time_now = datetime.time(int(timenow[0]),int(timenow[1]))
        issues.append(issue_id)
        issues.append(issue_desp)  
        issues.append(time_now)
        issues.append(role_issue)
    else:
        break
"""
print ('AGENT LIST: ',agent_list)
print ('AGENT ROLES: ',roles)
print ('ISSUES LIST: ',issues)
select_mode = ''
the_issue = []

def agent_select(agent_list,select_mode,the_issue):
    agent_reqd = []
    types_roles= (the_issue[3]).split(',')
    for k in range(len(types_roles)):
        for l in range(int(len(agent_list)/4)):
            if types_roles[k] == agent_list[(4*l +3)]:
                agent_reqd.append(agent_list[(4*l)])
                agent_reqd.append(agent_list[(4*l+1)])
                agent_reqd.append(agent_list[(4*l+2)])
                agent_reqd.append(agent_list[(4*l+3)])
        if types_roles[k] not in agent_list:
            print ('The role '+ types_roles[k] + ' is not available')
    # print('LIST OF AGENTS WITH ROLES RELATED TO THE ISSUE: ',agent_reqd)

    if select_mode == 'All available':
        print('For the issue:')
        print(the_issue)
        print('with selection mode:')
        print(select_mode)
        print('Here are the agents:')
        print(agent_reqd)
    
    if select_mode == 'Least busy':
        o = 0
        Diff = []
        timeDiff = 0
        for n in range(int(len(agent_reqd)/4)):
            A = datetime.datetime.combine(datetime.date.today(), the_issue[2])
            B = datetime.datetime.combine(datetime.date.today(), agent_reqd[(4*n+2)]) 
            timeDiff = A-B
            timeDiff = int(timeDiff.total_seconds())
            Diff.append(agent_reqd[(4*n)])
            Diff.append(timeDiff)
            if timeDiff > o :
                o = timeDiff
        # print('HIGHEST TIME DIFFERENCE BETWEEN THE ISSUE AND AVAILABILITY OF THE AGENT: ',o)        
        # print('LIST OF TIME DIFFERENCES: ',Diff)        
        for p in range(int(len(Diff)/2)):
            if o == Diff[2*p+1]:
                agent_reqd = agent_reqd[(4*p):(4*p+4)]
        print('For the issue:')
        print(the_issue)
        print('with selection mode:')
        print(select_mode)
        print('Here is the agent:')
        if o >0:
            print(agent_reqd)
        else:
            print('NIL')     
       
    if select_mode == 'Random':
        q = random.randrange(int(len(agent_reqd)/4))
        agent_reqd = agent_reqd[(4*q):(4*q+4)]
        print('For the issue:')
        print(the_issue)
        print('with selection mode:')
        print(select_mode)
        print('Here is the agent:')
        print(agent_reqd)


for m in range(int(len(issues)/4)):
    the_issue = issues[(4*m):(4*m+4)]
    print ('THE ISSUE: ',the_issue)
    select_mode = input('Select a selection mode (All available/Least busy/Random):')
    agent_select(agent_list,select_mode,the_issue)

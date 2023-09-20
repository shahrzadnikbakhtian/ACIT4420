# Problem 1
Create a program that stores your plans for a week. Each plan needs a start and an end-time, given to the nearest whole minute. You should choose between loading a plan, adding information to a plan, showing the current plan, and
saving the current plan.
The plan should be saved in a file, so you can load it again later with the
same program.
When showing the plan, you should only print the non-empty time-slots.
### Example use:
```bash
*Choose: load, add, show, save, exit
Choose from the list: add
Which day? Thursday
Start-time? 10:30
End-time? 12:15
What is the plan? ACIT4420 Lecture
*Choose: load, add, show, save, exit
Choose from the list: add
Which day? Thursday
Start-time? 12:30
End-time? 16:15
What is the plan? ACIT4420 Lab
*Choose: load, add, show, save, exit
Choose from the list: show
Which day? Wednesday
You have no plans for Wednesday.
*Choose: load, add, show, save, exit
Choose from the list: show
Which day? Thursday
Your plans for Thursday is:
10:30 - 12:15 ACIT4420 Lecture
12:30 - 16:15 ACIT4420 Lab
*Choose: load, add, show, save, exit
Choose from the list: save
File-name? ACITplans.txt
Your Calendar is saved.
*Choose: load, add, show, save, exit
Choose from the list: exit
Thank you, have a nice day.
```
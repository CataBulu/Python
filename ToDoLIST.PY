todo_list = []
while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  print ("Options:")
  print ("1) Add Task")
  print ("2) Remove Task")
  print ("3) Quit")
  choice = input()
  if choice == "1":
     print("Adding task\n")
     new_task = input("Enter the task\n")
     todo_list.append(new_task)
  elif choice == "2":
    print("Removing task")
    if len(todo_list) > 0:
      removed_task = todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break
  
    
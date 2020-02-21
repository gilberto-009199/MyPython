list = [];
while True:
  tty = int(input());
  if tty != 42 :
   list.append(tty);
  elif tty  == 42 :
   for item in list:
     print(item);
   exit();

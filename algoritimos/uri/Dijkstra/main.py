listJoias = [];
typeJoias = 0;
for joia in range(0,5) :
  tty = str(input());

  try:
    listJoias.index(tty) 
  except ValueError:
    typeJoias += 1;
  listJoias.append(tty);

print(typeJoias);

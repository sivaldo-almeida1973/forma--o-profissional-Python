def primo(numb):
  for i in range(2, numb):
    if (numb % i) == 0:
      return False
    return True
import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

  for x in range(0, 2):
    last = 13
    rnd = random.randint(0, last)
    print(quotes[rnd])

  with open('quotes.txt', 'a') as file:
    file.write('hey!!!!!' + '\n')


if __name__== "__main__":
  primary()

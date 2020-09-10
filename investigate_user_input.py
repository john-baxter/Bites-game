from constants import 

class GetName():
  def __init__(self):
    self.name = ""

  def get_name(self):
    while 1:
      name = input("Name: ")
      if name == "":
        print("Try again")
      else:
        print("Hello,", name)
        break
    self.name = name





# if __name__ == '__main__':
#   ask_for_name = GetName()
#   ask_for_name.get_name()
#   input("\n\nPress 'Enter' to exit")
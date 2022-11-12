print('''


                             _.---.
                      |\---/|  / ) ca|
          ------------;     |-/ /|foo|---
                      )     (' / `---'
          ===========(       ,'==========
          ||   _     |      |
          || o/ )    |      | o
          || ( (    /       ;
          ||  \ `._/       /
          ||   `._        /|
          ||      |\    _/||
        __||_____.' )  |__||____________
         ________\  |  |_________________
                  \ \  `-.
                   `-`---'  pandora
                   
                   *****************************
''')
print("Welcome to The Hungry Cat.")
print("Your mission is to find the cat food.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

food = input("You didn't eat for hours and you are starving. Choose between Sheeba or Fancy Feast:\n")
food_l = food.lower()
if food_l == "sheeba":
  print("Oh no! It was jelly. Cat go hungry. Game over!")
else:
  treat = input("Is it treat time? I am hungryyyy. Type Y or N:\n")
  if treat == "Y":
    print("Too late, Maya beat you to it. She ate them all. You lose")
  else:
    tw = input("Just one more step to fill this big belly, which color of Taste of the Wild is the best: Yellow, Green or Purple?\n")
    taste = tw.lower()
    if taste == "yellow":
      print("Well done. Time for a nap!")
    else:
      print("CAT IS ANGRY. NO CUDDLES TONIGHT")
      
print('''



       _
      ( \
       \ \
       / /                |\\
      / /     .-`````-.   / ^`-.
      \ \    /         \_/  {|} `o
       \ \  /   .---.   \\ _  ,--'
        \ \/   /     \,  \( `^^^
         \   \/\      (\  )
          \   ) \     ) \ \
      jgs  ) /__ \__  ) (\ \___
          (___)))__))(__))(__)))






''')



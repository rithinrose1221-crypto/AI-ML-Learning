# import numpy as np
# # # list1=np.array([1,2,3,4,5])
# # # print(list1)

# # zerodim=np.array(1)
# # print(zerodim.ndim)

# # onedim=np.array([1,2,3,4,5])
# # print(onedim.ndim)

# # twodim=np.array([[1,2,3],[4,5,6],[7,8,9]])
# # print(twodim.ndim)

# # threedim=np.array([[[1,2,3],[4,5,6],
# #                 [7,8,9]],[[10,11,12],
# #                 [13,14,15],[16,17,18]]])
# # print(threedim.ndim)

# # fourdim=np.array(
# #   [
# #     [[1,2,3],[4,5,6],[7,8,9]],
# #     [[0,1,2],[3,4,5],[6,5,8]],
# #     [[9,0,2],[4,5,3],[5,6,7]],
# #   ]
# #   )
# # print(fourdim[0,0]+fourdim[2,2])
# # print(fourdim[2,0]-fourdim[0,2])
# # print(fourdim[1,0]*fourdim[1,2])
# # print(fourdim[0,1]/fourdim[2,1])

# # fourdim=np.array(
# #   [
# #     [
# #       [1,2,3],[4,5,6],[7,8,9],
# #       [0,1,2],[3,4,5],[6,5,8],
# #       [9,0,2],[4,5,3],[5,6,7],
# #     ]
# #   ]
# #   )
# # print(fourdim[0,0]+fourdim[0,0])
# # print(fourdim[2,0]-fourdim[0,2])
# # print(fourdim[1,0]*fourdim[1,2])
# # print(fourdim[0,1]/fourdim[2,1])

# # import numpy as np

# # letter=[[['A','b','c'],['d','e','f'],['g','h','i']],
# #         [['j','K','l'],['m','n','o'],['p','q','r']],
# #         [['s','t','u'],['v','w','x'],['y','z',' ']]]

# # print(letter[0][0][0]+letter[1][0][0]+letter[0][2][2]+letter[1][1][1]+letter[2][2][2]+letter[1][0][1]+letter[2][0][2]
# #       +letter[1][1][0]+letter[0][0][0]+letter[1][2][2])



# # odd=np.array([1,3,5,7,9,11,13,15])

# # add=odd+3
# # print(add)


# # even=np.array([2,4,6,8,10,12,14])

# # sub=even-2
# # print(sub)

# # num=np.array([12.3,23.4,34.5,54.9])

# # roun=num.round()
# # print(roun)

# # cel=np.ceil(num)
# # print(cel)

# # flo=np.floor(num)
# # print(flo)


# # val=np.array([4,16,36])
# # sqr=np.sqrt(val)
# # print(sqr)


# # tab1=np.array([[1,2,3,4,5,6,7,8,9,10]]  )

# # tab2=np.array([[1],
# #               [2],
# #               [3],
# #               [4],
# #               [5],
# #               [6],
# #               [7],
# #               [8],
# #               [9],
# #               [10]
# #               ])

# # # print(tab1.shape)
# # # print(tab2.shape)
# # print(tab1*tab2)

# import numpy as np

# student=np.array([[9,8,7,5,8],
#                   [8,6,4,9,2],
#                   [5,7,2,3,5],
#                   [3,6,8,9,2],
#                   [4,7,3,9,1]])

# print(np.sum(student,axis=1))
# print(np.mean(student,axis=0))
# print(np.max(student))  
# print(np.min(student))
# print(np.argmax(student))
# print(f"Student total mark is",(np.sum(student, axis=1)),"Student Avgerage mark is",(np.mean(student)),"Student highest mark is ",(np.max(student)),"Student Lowest mark is",(np.min(student)))



# import numpy as np

# mark=np.array([
#                 [90,45,60,30,18,59],
#                 [67,80,57,49,21,13]])

# failed=np.where(mark<35,mark,0)
# print(failed)

# avgerage=np.where((mark>35) & (mark<70),mark,0)
# print(avgerage)

# toper=np.where(mark>70,mark,0)
# print(toper)

# print(f"failed student",failed,"avgerage student",avgerage,"top student",toper)


# import numpy as np

# rng=np.random.default_rng()

# print(rng.integers(low=1,high=15,size=3))

# print(rng.uniform(low=0,high=20,size=(2,2)))

# shu=np.array(["r","i","t","h","i","n"])
# rng.shuffle(shu)
# print(shu)

# import numpy as np

# move=np.array(["rock","paper","scissor"])
# player_choice=input("Enter your move:").lower()
# computer_choice=np.random.choice(move)

# print(player_choice)
# print(computer_choice)

# if(player_choice==computer_choice):
#     print("tie")
# elif(player_choice=="rock" and computer_choice=="scissor"):
#     print("player wins")
# elif(player_choice=="scissor" and computer_choice=="rock"):
#     print("computer wins")
# elif(player_choice=="rock" and computer_choice=="paper"):
#     print("computer wins")
# elif(player_choice=="paper" and computer_choice=="rock"):
#     print("player wins")
# elif(player_choice=="scissor" and computer_choice=="paper"):
#     print("player wins")
# elif(player_choice=="paper" and computer_choice=="scissor"):
#     print("computer wins")

# import numpy as np

# letter=[[['A','B','C'],['D','E','F'],['G','H','I']],
#         [['J','K','L'],['M','N','O'],['P','Q','R']],
#        [['S','T','U'],['V','W','X'],['Y','Z',' ']]]

# sletter=[[['A','b','c'],['d','e','f'],['g','h','i']],
#          [['j','K','l'],['m','n','o'],['p','q','r']],
#      [['s','t','u'],['v','w','x'],['y','z',' ']]]

# print(letter[0][2][2]+sletter[2][2][2]+letter[1][0][2]+sletter[1][1][2]+sletter[2][1][0]+sletter[0][1][1]+sletter[2][2][2]+letter[2][2][0]+sletter[1][1][2]+sletter[2][0][2])



'''----------------------------------PANDAS--------------------------------'''


'''
import pandas as pd

fruits=pd.Series(["apple","grapes","mango","orange"], index=["Fruits1","Fruits2","Fruits3","Fruits4"])
print(fruits)

print(fruits.loc["Fruits3"])

fruits.loc["Fruits2"]="Pineapple"
print(fruits)
'''
'''
import pandas as pd

student_data={
    "Name": ["rithinrose","ajinkumar","afsal","rio"],
    "Course":["AI/ML","UI/UX","Editing","Trading"],
    "Place": ["London","Manali","Dubai","Kollam"]
}

student=pd.DataFrame(student_data, index=['No1','No2','No3','No4'])
print(student)


new_student=pd.DataFrame([{"Name":"abi","Course":"AI Engineer","Place":"TamilNadu"}], index=['No5'])
std=pd.concat([student,new_student])
print(std)'''


'''import pandas as pd

Anime={
    "Name":["One piece","Attack on Titan","Naruto","Bleach","Solo Leveling"],
    "Genre":["Adventure","Thriller","Martial arts","action","fantasy-action"],
    "Rating":[10,9,5,7,3]
}
seriess=pd.DataFrame(Anime, index=[1,2,3,4,5])
print(seriess)

print(seriess[seriess["Rating"]>4])'''

# import pandas as pd

# tested=pd.read_csv('anime.csv')
'''print(tested.head())


  print(tested["name"].head(10))

  rate=tested[(tested["rating"]>9) & (tested["rating"]<9.5)]
  print(rate)

gen=tested[(tested["genre"]=="Comedy")]
print(gen)'''

# hii=tested["episodes"]
# print(type(hii))
# print(tested["episodes"].mean())
# print(tested["episodes"].sum())
# print(tested["episodes"].minn())
# print(tested["episodes"].max())





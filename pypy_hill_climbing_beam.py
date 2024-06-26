



import datetime
from random import randint

max_beam_value=5

stoping_count=10000

# file_name='a_an_example'
# file_name='b_basic'
# file_name='c_coarse'
# file_name='d_difficult'
file_name='e_elaborate'


# beam_value=5

use_old_output=False

use_old_output_file=f'output/{file_name}.out.txt'

file_name_in = f'{file_name}.in.txt'
# file_name_out=f'{file_name}.out.txt'



start = datetime.datetime.now()
# print(f'Started {start}')


Ingredients=[]
# Pizzas=[]
Clients=[]

# class Ingredient:
#     def __init__(self) -> None:
#         pass


# class Pizza:
#     def __init__(self) -> None:
#         pass

# class Client:
#     def __init__(self) -> None:
#         pass




def return_score(pizza):
    score=0
    for client in Clients:
    # print(client)

        if will_buy_pizza(client, pizza):
            score+=1

    return score



Lines=[]




with open(file_name_in, "r") as f:
    Lines = f.readlines()

# print(Lines)
# for line in Lines:
#     print(line)

num_of_clients=int(Lines[0])
print(f'num_of_clients: {num_of_clients}')



def create_ingredient(liked_ingredients):
    for i in range(len(liked_ingredients)):
        if liked_ingredients[i]  not in Ingredients:
            Ingredients.append(liked_ingredients[i])

    
#create ingredients
for i in range(1,len(Lines),2):

    liked_ingredients=Lines[i].split()[1:]
    disliked_ingredients=Lines[i+1].split()[1:]

    # print(liked_ingredients)
    # print(disliked_ingredients)

    create_ingredient(liked_ingredients)





print(f'Ingredients: {len(Ingredients)}')
# print(f'All Ingredients {Ingredients}')








def get_ingredient_name(index):
    return Ingredients[index]


def get_pizza_ingredient_name(pizza):
    return [get_ingredient_name(index) for index in pizza]



def get_ingredient_index_from_name(ingredient_name):

    # try:
    #     return Ingredients.index(ingredient_name)
    # except:
    #     return False


    for i, ingredient in enumerate(Ingredients) :

        if ingredient == ingredient_name:
            return i


def create_client(liked_ingredients,disliked_ingredients):

    
    clientobj=[
        [],
        [],
    ]


    # print(liked_ingredients)
    # print(disliked_ingredients)



    for liked_ingredient in liked_ingredients:
        # print(liked_ingredient)
        ingredient_index=get_ingredient_index_from_name(liked_ingredient)
        # print(ingredient_index)
        if ingredient_index is not None:
            clientobj[0].append(ingredient_index)

    for disliked_ingredient in disliked_ingredients:
        ingredient_index= get_ingredient_index_from_name(disliked_ingredient)
        if ingredient_index is not None:
            clientobj[1].append(ingredient_index)



    # print(f"liked_ingredients: {get_pizza_ingredient_name(clientobj[0])}")
    # print(f"disliked_ingredients: {get_pizza_ingredient_name(clientobj[1])}")



    Clients.append(clientobj)



    #create Clients
for i in range(1,len(Lines),2):

    liked_ingredients=Lines[i].split()[1:]
    disliked_ingredients=Lines[i+1].split()[1:]



    # print(liked_ingredients)
    # print(disliked_ingredients)

    # create_ingredient(liked_ingredients)
    create_client(liked_ingredients,disliked_ingredients)


print(len(Clients))



def will_buy_pizza(client, pizza):

    # print(f'Pizza: {get_pizza_ingredient_name(pizza)}')

    

    for liked_ingredient in client[0]:
        # print(f'liked: {get_ingredient_name(liked_ingredient)}')
        if liked_ingredient not in pizza:
            # print('not in pizza')
            return False

    for disliked_ingredient in client[1]:
        # print(f'disliked: {get_ingredient_name(disliked_ingredient)}')
        if disliked_ingredient in pizza:
            # print('in pizza')
            return False

    return True



# score=0

# with open(file_name_out, "r") as f:
#     Line = f.readline()

# pizza_lines=Line.split()[1:]

# print(f'Out Pizza: {pizza_lines}')

# pizza=[get_ingredient_index_from_name(pizza_ingredient) for pizza_ingredient in pizza_lines]

# for client in Clients:
#     # print(client)

#     if will_buy_pizza(client, pizza):
#         score+=1


max_pizza=[]
max_pizza_score=0


if use_old_output:

    

    with open(use_old_output_file, "r") as f:
        Line = f.readline()

    pizza_lines=Line.split()[1:]

    # print(f'Out Pizza: {pizza_lines}')
    print(f'Out Pizza Ingredients: {len(pizza_lines)}')

    max_pizza=[get_ingredient_index_from_name(pizza_ingredient) for pizza_ingredient in pizza_lines]



    max_pizza_score=return_score(max_pizza)



def make_max_pizza_random_clients_like():

    global max_pizza_score
    global max_pizza

    global max_beam_value

    beam_value=randint(1,max_beam_value)
    # temp_beams=[]

    temp_beam_pizza=max_pizza.copy()
    temp_pizza_score=0

    for i in range(beam_value):


        client = secrets.choice(Clients)



        

        for liked_ingredient in client[0]:
            # print(f'liked: {get_ingredient_name(liked_ingredient)}')
            if liked_ingredient not in temp_beam_pizza:
                # print('not in pizza')
                temp_beam_pizza.append(liked_ingredient)

        for disliked_ingredient in client[1]:
            # print(f'disliked: {get_ingredient_name(disliked_ingredient)}')
            if disliked_ingredient in temp_beam_pizza:
                # print('in pizza')
                temp_beam_pizza.remove(disliked_ingredient)

        
    temp_pizza_score = return_score(temp_beam_pizza)

        # temp_beams.append([temp_beam_pizza,temp_beam_score])


    


    # for temp_beam in temp_beams:

    #     if temp_beam[1] >=temp_pizza_score:
    #         temp_pizza_score=temp_beam[1]
    #         temp_max_pizza=temp_beam[0]
            


    
    if temp_pizza_score >= max_pizza_score:
        max_pizza_score=temp_pizza_score
        max_pizza=temp_beam_pizza




import secrets




# import  multiprocessing as mp

# pool = mp.Pool(4)

count=0

def hill_climb():
    global count
    count+=1
    if not count%100 :
        print(f"{count} {max_pizza_score}")


    make_max_pizza_random_clients_like()


def hill_climbing():

    

    

    while(count<stoping_count):
        hill_climb()


    # pool.map(range(stoping_count))


    # pool.map(pool_map, [row for row in range(stoping_count)])



        # if will_buy_pizza(client, max_pizza):
        #     pass
        # else:
            
        #     if will_buy_pizza(client, max_pizza):
        #         pass
        #     else:
        #         print("Can't make pizza client likes")

        





hill_climbing()
# print(max_index)

# max_pizza=pizza_combinations[max_index]


# print(max_pizza)

def make_pizza(pizza):
    return get_pizza_ingredient_name(pizza)




max_score=return_score(max_pizza)
output_pizza=make_pizza(max_pizza)

print(f'max score: {max_score}')

end = datetime.datetime.now()
# print(f'Ended {end}')

timetaken=end-start

file_name_out=f'output/{file_name}.out.{max_score}.txt'

# file_name_out=f'{file_name}.out.Score.{max_score}.Iteration.{stoping_count}.Time.{timetaken}.txt'


def save_pizza(pizza):
    
     with open(file_name_out,"w") as f:
        # L = ["This is Delhi \n","This is Paris \n","This is London"] 
        output=f'{len(pizza)}'
        f.write(output)

        for ingredient in pizza:
            output=f' {ingredient}'
            f.write(output)

        # f.writelines(output)

save_pizza(output_pizza)


print(f'Filename: {file_name}')
# print(f'Final Score: {score}')

print(f'num_of_clients: {num_of_clients}')
print(f'Ingredients: {len(Ingredients)}')




print(f'Time Taken {timetaken}')



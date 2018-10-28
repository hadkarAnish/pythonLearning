# Pseudocode #

# Take input from the user for number of actors
# Take input from the user for number of roles and attributes
# Create a matrix to store the value of each actor who has roles and attributes
#
# function weighted score with input as the score
#     calculate the weight of each score by taking the weight as input
#
# for rows in the matrix:
#     for columns in the matrix
#         Take input from the user for each actor's score
#         current cell = weighted score of each score entered
#
#
# for each row in the matrix:
#     print the sum of the weighted score for that actor


# Code snippet #

# Inputs
number_of_actors = int(input("Enter number of actors: "))
number_of_roles_and_attributes = int(input("Enter number of roles and attributes: "))
# initialize the matrix that holds the "table" for each actor and the actor's role/attribute
Matrix = [[0 for x in range(number_of_roles_and_attributes)] for y in range(number_of_actors)]


# calculate the weighted score
def weighted_score(score):
    weight = 0.0

    weight = float(input("Enter the weight = "))
    return float(score)*weight


# add items to the array
for i in range(number_of_actors):
    for j in range(number_of_roles_and_attributes):
        Matrix[i][j] = weighted_score(input("Enter score for the role: "))

# Calculate the total weighted score of each actor
for i in range(number_of_actors):
    print("total weighted score of the actor: " + str(sum(Matrix[i])))



# print([i[1] for i in Matrix])
# print(Matrix)

# for i in range(number_of_actors):
#     print("row " + str(i))
#     for j in range(number_of_roles):
#         print(" column value:" + str(Matrix[i][j]))




# actor_weight = [-0.7,0.8]
# role_weight = [x * 0.5 for x in actor_weight]
# print(role_weight)
# role_weight = [0.4,0.4]
#
# # No iterables are passed
# result = zip()
#
# # Converting itertor to list
# resultList = list(result)
# print(resultList)

# for g in range(len(actor_weight)):
#     actor_weight[g] = actor_weight[g] * role_weight[g] / sum(role_weight)
# print(sum(actor_weight))

# Two iterables are passed
# result = zip(actor_weight, role_weight)

# print(sum(x * y for x, y in zip(actor_weight, role_weight))/sum(role_weight))

# Converting itertor to set
# resultSet = set(result)
# print(resultSet)

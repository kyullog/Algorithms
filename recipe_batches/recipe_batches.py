#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    lowest_batch = math.inf

    try:
        for i in recipe:
            batch = ingredients[i] // recipe[i]
            if batch < lowest_batch:
                lowest_batch = batch
    except(KeyError):
        return 0

    return lowest_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 400, 'butter': 125, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# Deleting Book Named Nineteen Eighty-Four

delete= Book.objects.filter(title= 'Nineteen Eighty-Four').delete()
""" #Output:
title |    author     | publication_year
NULL       NULL            NULL
"""

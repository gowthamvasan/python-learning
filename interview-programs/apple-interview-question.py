'''We have a nested object, we would like a function that you pass in the object and a key and
get back the value. How this is implemented is up to you.
Example Inputs
object = {"a":{"b":{"c":"d"}}}
key = a/b/c
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a
Hints:
We would like to see some tests. A quick read to help you along the way
We would expect it in any other language apart from elixir.
A quick read to help you along the way
'''
def check_dict(md,search_key):
    # pdb.set_trace()
    if search_key in md.keys():
       print(search_key,"--" ,md[search_key])
       return

    for key,val in md.items():
         if type(val) is dict:
            check_dict(val,search_key)

    return None

if __name__=="__main__":
   md = {"a":{"b":{"c":"d"}}}
   check_dict(md,'c')
import pandas as pd



def colour_dtype(val):
    a= 3
    b= 3.0
    c= 'str'

    int_types = type(a)
    float_types = type(b)
    object_types = type(c)
    if type(val) == int_types:
        return 'background-color: red'
    elif type(val) == float_types:
        return 'background-color: green'
    else:
        return 'background-color: orange'
    
def get_mem_usage(pd_obj):
    if isinstance(pd_obj, pd.Dataframe):
        mem_use = pd_obj.memory_usage(deep=True).sum()
    else:
        mem_use = pd_obj.memory_usage(deep=True)
    
    mem_use_mb = mem_use/1024**2
    
    return "{03:2f} MB".format(mem_use)
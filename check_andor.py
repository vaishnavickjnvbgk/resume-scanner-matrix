def cond_or(res_dct,field,x,y):
        if x in [i.strip() for i in res_dct[field].lower().split(",")] or y in [i.strip() for i in res_dct[field].lower().split(",")]:
            return True
        else:
            return False
def cond_and(res_dct,field,x,y):
        if x in [i.strip() for i in res_dct[field].lower().split(",")] and y in [i.strip() for i in res_dct[field].lower().split(",")]:
            return True
        else:
            return False
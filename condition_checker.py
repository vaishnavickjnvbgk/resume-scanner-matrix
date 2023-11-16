import check_andor
import check_experience
def check_condition(res_dct,condition,field):
                        
                        if field.lower() not in res_dct:
                            print(field)
                            return "-1"
                        else:
                            if(field=="total_exp"):
                                val=check_experience.experience(res_dct,condition[0],field)
                                if val:
                                    return True
                                elif val=="invalid":
                                    return "-1"
                            else:
                                l=condition.lower().split(" ")
                                print(l)
                                if len(l)==1:
                                    if l[0].strip() in [i.strip() for i in res_dct[field].lower().split(",")]:
                                        return True
                                    else:
                                        return False
                                
                                for i in range(1,len(l),2):
                                    print("and",l[i])
                                    if l[i]=="and":
                                        
                                        temp=check_andor.cond_and(res_dct,field,l[i-1].lower().strip(),l[i+1].lower().strip())
                                        print(temp)
                                        if not temp:
                                            return False
                                    elif l[i]=="or":        
                                        temp=check_andor.cond_or(res_dct,field,l[i-1].lower().strip(),l[i+1].lower().strip())
                                        
                                        if not temp:
                                            return False
                                    else:
                                        return "-1"
                                return True

def experience(res_dct,condition,field):
    if '>' in condition:
                            if ">=" in condition: 
                                ndeg=condition.replace(">=", '').strip()
                                print(ndeg)
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())>=ndeg):
                                        return True
                                else:
                                    return "invalid"
                            else:
                                ndeg=condition.replace('>', '').strip()
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())>ndeg):
                                        return True
                                else:
                                    return "invalid"
    elif '<' in condition: 
                            if "<=" in condition: 
                                ndeg=condition.replace("<=", '').strip()          
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())<=ndeg):
                                        return True
                                else:
                                    return "invalid"
                            else:
                                ndeg=condition.replace('<', '').strip()
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())<ndeg):
                                        return True
                                else:
                                    return "invalid"
    elif '=' in condition: 
                            ndeg=condition.replace('=', '').strip()
                            if ndeg.isdigit():
                                if((res_dct["total_exp"].strip())==ndeg):
                                    return True
                            else:
                                return "invalid"
                        
    else:
        return "invalid"

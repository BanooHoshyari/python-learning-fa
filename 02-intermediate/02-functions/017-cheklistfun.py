#تابع که چک میکند لیست فقط عدد میباشد
#def all_numbers(lst):
 #   return all(isinstance(x, (int, float)) for x in lst)
#lis=[2,3]

def chklist(l:list):
    if not isinstance(l,list):
        return False
    else:   
        for i in l:
            if  not isinstance(l,list):
                return False
            else:
                for i in l :
                    if not isinstance(i,int)or not isinstance(i,flat):
                        return False
                    else:
                        return True

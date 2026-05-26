def main():
    dic = list_to_dic(grocery_list())
    for item in dic:
        print(dic[item], item.upper())



def grocery_list():
    grocery_list = []
    while True:
        try:
            item = input("Item: ").strip().lower()
            grocery_list.append(item)
        except KeyboardInterrupt:
            print()
            return grocery_list
        

def list_to_dic(lst):
    grocery_dic = {}
    for item in lst:
        grocery_dic[item] = 0
    for item in lst:
        grocery_dic[item] += 1
    return grocery_dic

main()




import pickle
data=['one',2,[3,4,5],lambda l:1]

with open('data1.txt','wb') as f:
    try:
        pickle.dump(data,f)
    except pickle.PicklingError:
        print("Error while reading object")

# objdump=None

# with open('data.txt','rb') as f:
#     objdump=pickle.load(f)
#     print(objdump)
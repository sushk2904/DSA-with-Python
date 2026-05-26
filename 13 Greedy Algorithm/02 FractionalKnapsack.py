val = [60,100,200,100]
wt = [10,20,50,50]
capacity = 90
#first of all you need to combine them either using zip method or for loop
combined_array = [(val[i], wt[i]) for i in range(len(val))]
# or just use combined_array = list(zip(val,wt))
curr_wt = 0
final_val = 0
#We need to sort them to find the fraction and also we will sort them and then reverse them since python does sorting in ascending way
combined_array.sort(key = lambda x: x[0]/x[1], reverse = True)
for v,w in combined_array:
    if curr_wt + w <= capacity:
        curr_wt = curr_wt + w
        final_val = final_val + v
    else:
        remain = capacity - curr_wt
        cost = v/w * remain
        final_val = cost + final_val
        break
print(final_val)
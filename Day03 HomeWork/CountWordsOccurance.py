def count_occurances(st):
     occurance=dict()
     words=st.split(' ')
     for word in words:
         if word in occurance :
             occurance[word]+=1
         else:
             occurance[word]= 1
     return occurance
a  = input()
print(count_occurances(a))
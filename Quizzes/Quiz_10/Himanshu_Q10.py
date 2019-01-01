def preferred_sequence():
    listk=[pq._data[k] for k in range(1,pq._length+1)]
    listk=sorted(listk,reverse=True)
    #print(listk)
    final_list=[]
    if len(listk)>=3:
        while pq._length!=3:
            #print("listk", listk)
            for k in listk:
                nb_of_elements=pq._length
                position=nb_of_elements
                #print("k ",k)
                list_position_path=[]
                while position>=1:
                    list_position_path.append(position)
                    #print(position)
                    position=position//2
                    if position==1:
                        break
                #print("yes") 
                list_position_path.append(1)
                #print("k ", k)
                flag=0
                for element in list_position_path:
                    if pq._data[element]==k:
                        flag=1
                        break
                possibility=1
                put=[]
                if flag==1:
                    list_position_path=sorted(list_position_path)
                    #print("list_position_path", list_position_path)
                    i=0
                    to_be_put_position=0
                    while pq._data[to_be_put_position]!=k:
                        if i==0:
                            last_position=list_position_path.pop()
                            to_be_put_position=list_position_path.pop()
                        else:
                            if list_position_path!=[]:
                                to_be_put_position=list_position_path.pop()
                        if last_position%2==1:#check if how many child does his parent have
                            if pq._data[last_position]>pq._data[last_position-1]:
                                put.append((last_position,to_be_put_position,pq._data[last_position]))
                            else:
                                possibility=0
                                break
                        else:
                            if last_position==pq._length:
                                put.append((last_position,to_be_put_position,pq._data[last_position]))
                            else:
                                if pq._data[last_position+1]!=None:
                                    if pq._data[last_position]>pq._data[last_position+1]:
                                        put.append((last_position,to_be_put_position,pq._data[last_position]))
                                    else:
                                        possibility=0
                                        break
                                else:
                                    put.append((last_position,to_be_put_position,pq._data[last_position]))
                        last_position=to_be_put_position
                        i+=1
                else:
                    continue
                if possibility==0:
                    continue
                else:
                    #print("put ", put)
                    for put_element in put:
                        #print("put_element ", put_element)
                        a=put_element[0]
                        b=put_element[1]
                        c=put_element[2]
                        #self.heap[a]=None
                        pq._data[b]=c
                    #print("self.heap", self.heap)
                    pq._length-=1
                    final_list.append(k)
                    #print("self.nb_of_elements ", self.nb_of_elements)
                    listk.remove(k)
                    break
        if pq._data[pq._length]>pq._data[pq._length-1]:
            final_list.append(pq._data[1])
            final_list.append(pq._data[3])
            final_list.append(pq._data[2])
        else:
            final_list.append(pq._data[3])
            if pq._data[2]>=pq._data[1]:
                final_list.append(pq._data[2])
                final_list.append(pq._data[1])
            else:
                final_list.append(pq._data[1])
                final_list.append(pq._data[2])
    else:
        if len(listk)==2:
            if pq._data[2]>=pq._data[1]:
                final_list.append(pq._data[2])
                final_list.append(pq._data[1])
            else:
                final_list.append(pq._data[1])
                final_list.append(pq._data[2])
        else:
            final_list.append(pq._data[1])
    #print(final_list)
    final_list_sorted=[]
    #len_final_list=len(final_list)-1
    for els in reversed(final_list):
        final_list_sorted.append(els)
    return final_list_sorted

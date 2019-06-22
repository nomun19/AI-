#Хот бүр дээр хөрш холбоотой орнуудыг хадгалдаг dic бөгөөд тухайн хотын нэрийг 
#бас хаанаас хаашаа хэр зайтайг хадгалдаг мод бүтэцтэй 
class Node():
    def __init__(self,nm):
        self.name=nm
        self.neighbors={}
    
    def __str__(self):
        return "" + str(self.name) + " horshuud " + str([x.name for x in self.neighbors])
    #холбоотой хотуудыг хадгалдаг 
    def add(self,child,weight=0):
        self.neighbors[child]=weight;
    #хотын нэрийг буцаадаг 
    def getName(self):
        tempa = self.name
        return str(tempa)
    #2 хотын хоорондох зайг буцаах
    def getWeight(self,child):
        return self.neighbors[child];
#Hotuudiig hadgalah graph classiin todophoilolot
class Graph:
    #Хөрш хотуудаа хадгалдаг хотын мэдээллийг хадгалдаг dic-тэй 
    #мөн хэдэн мод бүтэцтэй хотуудыг хадгалсан байгаа мэдээллийг хадгалдаг хувьсагч 
    def __init__(self):
        self.list={}
        self.listSize=0
        #өмнөх ирсэн хотоо хадгалах dic
        self.parentDict={}
    def __iter__(self):
        return iter(self.list.values())
    def length(self):
        return self.listSize
    #хотуудыг хадгалах dic рүүгээ хотыг хадгалах func мөн
    #dic-ийнхээ хэмжээг 1ээр нэмэгдүүлнэ
    def add_node(self,node):
        self.listSize = self.listSize+1
        tmp=Node(node)
        self.list[node]=tmp
        return tmp
    #нийт dic-д байх хотуудын dic-ийг буцаах func
    def get_node(self,n):
        if n in self.list:
            return self.list[n]
        else: 
            return None
    #haanaas haashaag gegdiig hadgalah bogood hariltsan upvuulj hadgalah func
    def add_edge(self,frm, to ,cost=0):
        if frm not in self.list:
            self.add_node(frm)
        if to not in self.list:
            self.add_node(to)
        self.list[frm].add(self.list[to],cost)
        self.list[to].add(self.list[frm],cost)
    
    def get_list(self):
        return self.list.keys()
    #1 хотоос нөгөө хотод очих хамгийн богино замыг олох func
    def BellmanFord(self, start,end):
        #Богино замуудын уртуудыг хадгалах dictionary
        path = {}
        # Хот болгон руу хүрэх замын уртыг 999999 болгоно
        for city, nd in self.list.items():
            path[city] = 999999
        # Эхлэл хотоос алслагдах зайг 0 болгоно
        path[start]=0
        # Хотын тоогоор давтаж бүх хот хүртэлх зайг олно
        for i in range(self.listSize):
            # Графын хот бүрээр гүйнэ
            for name, node in self.list.items():
                # хотуудын хөрш бүрээр гүйнэ
                for desmond, weighs in node.neighbors.items():    
                    # Хэрэв тус хөрш рүү очих замыг тодорхойлсон ба хуучин замаас дөтөөр очих боломжтой бол
                    if path[name] != 999999 and path[name]+ weighs < path[desmond.name]:
                        # Тус хөрш рүү очих замын уртыг шинэчилнэ
                        path[desmond.name] = path[name] + weighs
                        # Тухайн хөрш рүү очих замын хүснэгтэд утга нэмнэ
                        self.parentDict[desmond.name] = name
    # Богино замыг олж хэвлэх функц
    def printShortestPath(self, start, end):
        # Богино замыг хадгалах dictionary
        self.arr = {}
        # Богино замуудыг олох функцийг дуудна
        self.BellmanFord(start, end)
        # Богино замын дамжиж буй хотуудын нэрсийг хадгалах хүснэгт
        tempArr = []
        # Очих замын нэр гарж иртэл хүснэгтэд замд дайрж буй хотын нэрийг нэмнэ
        while start != end:
            tempArr.append(end)
            end = self.parentDict[end]
        tempArr.append(start)
        # Тус хүснэгтийг хэвлэнэ
        for elm in reversed(tempArr):
            print(elm)
        
      
                    
        

if __name__ == '__main__':
    g= Graph()
    
    
    """
    g.add_node("Vancouver")
    g.add_node("Calgary")
    g.add_node("Seattle")
    g.add_node("Helena")
    g.add_node("Winnipeg")
    g.add_node("Atlanta")
    g.add_node("Boston")
    g.add_node("Charleston")
    g.add_node("Chicago")
    g.add_node("Dallas")
    g.add_node("Denver")
    g.add_node("Duluth")
    g.add_node("El Paso")
    g.add_node("Helena")
    g.add_node("Houston")
    g.add_node("Kansas City")
    g.add_node("Las Vegas")
    g.add_node("Little Rock")
    g.add_node("Los Angeles")
    g.add_node("Miami")
    g.add_node("Montreal")
    g.add_node("Nashville")
    g.add_node("New Orleans")
    g.add_node("New York")
    g.add_node("Oklahoma City")
    g.add_node("Omaha")
    g.add_node("Phoenix")
    g.add_node("Pittaburgh")
    g.add_node("Portland")
    g.add_node("Raleigh")
    g.add_node("Saint Louis")
    g.add_node("Salt Lake City")
    g.add_node("San Francisco")
    g.add_node("Santa Fe")
    g.add_node("Sault Ste Marie")
    g.add_node("Toronto")
    g.add_node("Washington") 
    """
    
    # Өгөгдөл оруулах хэсэг
    g.add_edge("Vancouver","Calgary",150)
    g.add_edge("Vancouver", "Seattle", 45)
    g.add_edge("Calgary", "Seattle", 118)
    g.add_edge ("Calgary", "Helena", 130)
    g.add_edge("Winnipeg", "Helena", 137)
    g.add_edge("Calgary", "Winnipeg", 180)
    g.add_edge("Winnipeg", "Duluh", 103)
    g.add_edge("Winnipeg", "Sault Ste Marie", 156)
    g.add_edge("Sault Ste Marie", "Duluh", 110)
    g.add_edge("Sault Ste Marie", "Toronto", 90)
    g.add_edge("Sault Ste Marie", "Montreal", 193)
    g.add_edge("Toronto", "Pittsburgh", 80)
    g.add_edge("Toronto", "Montreal", 115)
    g.add_edge("Montreal", "New York", 99)
    g.add_edge("Montreal", "Boston", 69)
    g.add_edge("Boston", "New York", 74)
    g.add_edge("Seattle", "Portland", 44)
    g.add_edge("Seattle", "Helena", 189)
    g.add_edge("Helena", "Salt Lake City", 116)
    g.add_edge("Helena", "Denver", 126)
    g.add_edge("Helena", "Omaha", 174)
    g.add_edge("Helena", "Duluh", 150)
    g.add_edge("Duluh", "Omaha", 74)
    g.add_edge("Duluh", "Chicago", 157)
    g.add_edge("Chicago", "Pittsburgh", 81)
    g.add_edge("Chicago", "Omaha", 142)
    g.add_edge("Chicago", "Saint Louis", 104)
    g.add_edge("Pittsburgh", "New York", 69)
    g.add_edge("Pittsburgh", "Washington", 85)
    g.add_edge("Washington", "Raleigh", 47)
    g.add_edge("Portland", "San Francisco", 151)
    g.add_edge("New York", "Washington", 76)
    g.add_edge("Portland", "Salt Lake City", 175)
    g.add_edge("Salt Lake City", "San Francisco", 156)
    g.add_edge("Salt Lake City", "Las Vegas", 89)
    g.add_edge("Salt Lake City", "Denver", 101)
    g.add_edge("Denver", "Phoenix", 128)
    g.add_edge("Denver", "Santa Fe", 70)
    g.add_edge("Denver", "Kansas City", 135)
    g.add_edge("Denver", "Omaha", 130)
    g.add_edge("Kansas City", "Oklahoma City", 61)
    g.add_edge("Kansas City", "Saint Louis", 68)
    g.add_edge("Saint Louis", "Little Rock", 60)
    g.add_edge("Saint Louis", "Nashville", 85)
    g.add_edge("Nashville", "Raleigh", 128)
    g.add_edge("Nashville", "Atlanta", 67)
    g.add_edge("Raleigh", "Atlanta", 96)
    g.add_edge("Raleigh", "Charleston", 95)
    g.add_edge("San Francisco", "Los Angeles", 100)
    g.add_edge("Los Angeles", "Las Vegas", 66)
    g.add_edge("Los Angeles", "Phoenix", 109)
    g.add_edge("Los Angeles", "El Paso", 191)
    g.add_edge("Phoenix", "Santa Fe", 85)
    g.add_edge("Santa Fe", "El Paso", 65)
    g.add_edge("Santa Fe", "Oklahoma City", 121)
    g.add_edge("Oklahoma City", "Little Rock", 72)
    g.add_edge("Nashville", "Little Rock", 94)
    g.add_edge("Little Rock", "Dallas", 74)
    g.add_edge("Little Rock", "New Orleans", 100)
    g.add_edge("Atlanta", "Charleston", 63)
    g.add_edge("Atlanta", "Miami", 116)
    g.add_edge("Atlanta", "New Orleans", 120)
    g.add_edge("Charleston", "Miami", 80)
    g.add_edge("El Paso", "Dallas", 140)
    g.add_edge("Dallas", "Houston", 46)
    g.add_edge("Houston", "New Orleans", 80)
    g.add_edge("New Orleans", "Miami", 151)
    


    #for v in g:
    #    print(g.list[v.getName()])
    #print ('%s' %( g.list[v.getName()]))
    # Хэрэглэгчтэй харилцах хэсэг
    start = input("Ehleh hot: ")
    end = input("Ochih hot: ")
    g.printShortestPath(start, end)
    

    
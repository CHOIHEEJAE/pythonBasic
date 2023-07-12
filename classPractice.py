
class House :
    def __init__ (self, location, house_type, deal_type, price, completion_year) :
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
    # 매물정보 표시
    def show_detail(self) :
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
        
        
houses =[]
house1 = House("강남", "아파트", "매매", "20억", "2020년")
house2 = House("마포", "오피스텔", "전세", "5억", "2023년")
house3 = House("중랑", "빌라", "월세", "500/50", "2015년")
house4 = House("월계", "아파트", "매매", "8억", "2007년")

houses.append(house1)
houses.append(house2)
houses.append(house3)
houses.append(house4)

print("총 {0} 대의 매물이 있습니다.".format(len(houses)))

for house in houses :
    house.show_detail()

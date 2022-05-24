class ques:
    def __init__(self):
        self.perPersonWater = 10
        self.totalWater_2BHK = 900
        self.totalWater_3BHK = 1500
        self.corporation_Water = 0
        self.borewell_water = 0
        self.totalGuests = 0

    def allot_water(self, apartmentType, ratio):
        totalRatio = sum(ratio)
        if apartmentType == 2:
            self.corporation_Water = (self.totalWater_2BHK * ratio[0]) // totalRatio
            self.borewell_water = (self.totalWater_2BHK*ratio[1]) // totalRatio
        else:
            self.corporation_Water = (self.totalWater_3BHK * ratio[0]) // totalRatio
            self.borewell_water = (self.totalWater_3BHK*ratio[1]) // totalRatio
    
    def add_guests(self, guestCount):
        self.totalGuests += guestCount
    
    def bill(self):
        #Cost and water consumed for family members
        totalBillForFamily = self.corporation_Water*1 + self.borewell_water*1.5
        waterRequiredForFamily = self.corporation_Water + self.borewell_water

        #Cost and water consumed for guests
        waterRequiredForGuests = self.totalGuests*10*30
        if waterRequiredForGuests >= 0 and waterRequiredForGuests <= 500:
            totalBillForGuests = waterRequiredForGuests*2
        elif waterRequiredForGuests <= 501 and waterRequiredForGuests <= 1500:
            totalBillForGuests = 500*2 + (waterRequiredForGuests-500)*3
        elif waterRequiredForGuests <= 1501 and waterRequiredForGuests <= 3000:
            totalBillForGuests = 500*2 + (waterRequiredForGuests-500)*3 + (waterRequiredForGuests-1500)*5
        else:
            totalBillForGuests = 500*2 + (waterRequiredForGuests-500)*3 + (waterRequiredForGuests-1500)*5 + (waterRequiredForGuests-3000)*8

        #Overall calculation
        overallWaterRequired = waterRequiredForGuests + waterRequiredForFamily
        overallBill = totalBillForFamily + totalBillForGuests

        return overallWaterRequired, int(overallBill)

if __name__ == "__main__":
    water = ques()
    water.allot_water(3,[2,1])
    water.add_guests(4)
    water.add_guests(1)
    res = water.bill()
    print(res)



        



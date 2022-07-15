class Bank:
    def __init__(self, balance):
        self.dic = {}
        for i in range(1, len(balance)+1):
            self.dic[i] = balance[i-1]
            

    def transfer(self, account1, account2, money):
        if self.dic.get(account1, -1) != -1 and self.dic.get(account2, -1) != -1 and self.dic[account1] >= money:
                self.dic[account1] -= money
                self.dic[account2] += money
                return True
        return False
        
        

    def deposit(self, account, money):
        if self.dic.get(account, -1) != -1:
            self.dic[account] += money
            return True
        return False
            
    def withdraw(self, account, money):
        if self.dic.get(account, -1) != -1 and self.dic[account] >= money:
                self.dic[account] -= money
                return True
        return False



#Test Case:
#["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
#[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

#Complexity:
#Time: O(n)
#Space: O(n)



     

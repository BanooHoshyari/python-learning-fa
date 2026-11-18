import time
class Heater:
    def on_(self):
       return "the heater is ON"
    def off_(self):
        return "the heater is OFF"
    def warmig_on(self,temp):
        now_temp=10
        while (now_temp<temp):
            now_temp+=1
            print(now_temp)
            time.sleep(1)
        print(self.off_())


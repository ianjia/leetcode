# Hardcode Digits (better solution below)
class Solution1(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ""
        
        onesDict = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        tensDict = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        hundredsDict = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        thousandsDict = {1: "M", 2: "MM", 3: "MMM"}
        
        listNum = []
        result = []

        while num != 0:
            listNum.append(num % 10)
            num /= 10
        # Note: listNum will be reversed of num
        
        for i in range(0, len(listNum)):
            key = listNum[i]
            if key == 0:
                continue
            if i == 3:
                result.append(thousandsDict[key])
            elif i == 2:
                result.append(hundredsDict[key])
            elif i == 1:
                result.append(tensDict[key])
            else:
                result.append(onesDict[key])
            
        return "".join(result[::-1])

# Hardcode Digits (better solution)
class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]
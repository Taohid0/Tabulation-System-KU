class CalculateResult:
    def calculate(self,marks):
        if marks<40:
            return 0.00,"F"
        elif marks>=40 and marks <45:
            return 2.00,"D"
        elif marks>=45 and marks<50:
            return 2.25,"C"
        elif marks>=50 and marks<55:
            return 2.50,"C+"
        elif marks>=55 and marks<60:
            return 2.75,"B-"
        elif marks>=60 and marks<65:
            return 3.00,"B"
        elif marks>=65 and marks<70:
            return 3.25,"B+"
        elif marks>=70 and marks<75:
            return 3.50,"A-"
        elif marks>=75 and marks<80:
            return 3.75,"A"
        else:
            return 4.00,"A+"
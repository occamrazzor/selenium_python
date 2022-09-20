from oop_fun import Calculator


class ChildInherit(Calculator):
	num2 = 200
	def __init__(self):
		Calculator.__init__(self, 2, 10)

	def getCompleteData(self):
		return self.num2 + self.num + self.Summation()


obj = ChildInherit()
print(obj.getCompleteData())
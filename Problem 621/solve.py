lines = input()

encypted_results = []

for i in range(0,lines):
	curr_result = input()
	encypted_results.append(str(curr_result))

for result in encypted_results:
	# positive result
	if result == "1" or result == "4" or result == "78":
		print("+") 

	# negative result
	if result.endswith("35"):
		print("-")

	# Failed
	if result.startswith("9") and result.endswith("4"):
 		print ("*")

 	# Not Completed
 	if result.startswith("190"):
 		print("?")
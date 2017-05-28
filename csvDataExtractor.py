import re
import sys
import cStringIO

count = 0
avg_res_time = 0
avg_byte_sent = 0
health_check_count = 0
uni_users_count = 0

def Filename(filename):
	f = open(filename,'rU')

	def Avg_res_time():
		f.seek(0,0)
		global count
		global avg_res_time
		for line in f:
			match = re.search(r' GET (\S+)',line)
			if match:
				path = match.group(1)
				if 'onnow' in path:
					word = line.split(' ')
					count += 1
					avg_res_time = avg_res_time + int(word[-1])
		return avg_res_time/count

	def Avg_byte():
		f.seek(0,0)
		global count
		global avg_byte_sent
		for line in f:
			match = re.search(r' GET (\S+)',line)
			if match:
				path = match.group(1)
				if 'onlater' in path:
					word = line.split(' ')
					count += 1
					try:
						avg_byte_sent = avg_byte_sent + int(word[-2])
					except ValueError:
						pass
		return avg_byte_sent/count
	
	def  Health():
		f.seek(0,0)
		global health_check_count

		for line in f:
			match = re.search(r' GET (\S+)',line)
			if match:
				path = match.group(1)
				if '/health' in path:
					word = line.split(' ')
					health_check_count += 1
		return health_check_count

	def Uni_user():
		f.seek(0,0)
		global uni_users_count
		for line in f:
			match = re.search(r' GET (\S+)+\s+(\S+)+\s+(\S+)+\s+(\S+)+\s+(\S+)+\s+(\S+)',line)
			if match:
				path = match.group(6)
				if '5.0' in path:
					word = line.split(' ')
					uni_users_count += 1
		return uni_users_count

	#def Top_providers():
		#for line in f:
			#match = re.search(r' GET (\S+)',line)
			#if match:
				#path = match.group(1)
				#if 'onnow' or 'onlater' in path:
					#if 'userId' and 'providerId' in path:
						#word = line.split(' ')

	print 'Avg_res_time:',Avg_res_time()
	print 'Avg_byte:',Avg_byte()
	print 'Health:',Health()
	print 'Uni_user:',Uni_user()

	f.close()

def main():
	args = sys.argv[1:]
	for arg in args:
		Filename(arg)

if __name__ == '__main__':
	main()

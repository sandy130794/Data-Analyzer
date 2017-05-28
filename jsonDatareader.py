import json
import sys

def Filename(filename):
	data_file = open(filename,'rU') 
	data = json.load(data_file)
	#print data


	def like():
		data_file.seek(0,0)
		likes_count = 0
		if "groups" in data["response"]:
				#print data["response"]["groups"]
				if "items" in data["response"]["groups"][0]:
					#print data["response"]["groups"][0]["items"]  # for items enter the index value
					for tip in data["response"]["groups"][0]["items"]:
						if "tips" in tip:
							#print tip["tips"]
							for lks in tip["tips"]:
								if "likes" in lks:
									#print lks["likes"]
									if "count" in lks["likes"]:
										#print lks["likes"]["count"]
										likes_count = lks["likes"]["count"] + likes_count
		return likes_count

	def venue():
		lst = []
		data_file.seek(0,0)
		if "groups" in data["response"]:
				#print data["response"]["groups"] 
				if "items" in data["response"]["groups"][0]:
					#print data["response"]["groups"][0]["items"]  # for items enter the index value
					for vnue in data["response"]["groups"][0]["items"]:
						if "venue" in vnue:
							#print vnue["venue"]
							#if "id" in vnue["venue"]:
								print vnue["venue"]["name"]



	print "likes_count:",like()
	#print "venue_name:\n",venue()
	venue()


def main():
	args = sys.argv[1:]
	for arg in args:
		Filename(arg)

if __name__ == '__main__':
	main()
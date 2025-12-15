import requests
import sys

def main():
	nb_of_btc = get_av1()
	try:
		r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8da9061554c934127a0ebf2c4dbed23f71896469d18ccb22210d64c06a34f18d")
	except requests.RequestException:
		sys.exit("Get request error")

	response = r.json()
	price = float(response["data"]["priceUsd"])
	res = nb_of_btc * price
	print(f"${res:,.4f}")


def get_av1():
	if len(sys.argv) != 2:
		sys.exit("Missing command line argument")
	try:
		res = float(sys.argv[1])
	except ValueError:
		sys.exit("Command line argument is not a number")
	return res



if __name__ == "__main__":
	main()
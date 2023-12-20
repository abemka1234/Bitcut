import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def is_bitlink(token, link):
	payload = {"Authorization": f"Bearer {token}"}
	bitlink_parts = urlparse(link)
	cutted_bitlink = "{}{}".format(bitlink_parts.netloc,bitlink_parts.path)
	response = requests.get("https://api-ssl.bitly.com/v4/bitlinks/{0}".format(cutted_bitlink),headers=payload)
	return response.ok


def shorten_link(token, link):
	link = {"long_url": link}
	payload = {"Authorization": f"Bearer {token}"}
	response = requests.post("https://api-ssl.bitly.com/v4/bitlinks", json=link, headers=payload)
	response.raise_for_status()
	return response.json()["link"]


def count_clicks(token, bitlink):
	payload = {"Authorization": f"Bearer {token}"}
	bitlink_parts = urlparse(bitlink)
	cutted_bitly = "{}{}".format(bitlink_parts.netloc,bitlink_parts.path)
	link = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(cutted_bitly)
	response = requests.get(link, headers=payload)
	response.raise_for_status()
	return response.json()["total_clicks"]


if __name__ == '__main__':	
	parser = argparse.ArgumentParser(description='Link to Bitlink,Or get number of clicks on your bitlink')
	parser.add_argument('link', help='link,that will changed or you will get number of clicks')
	args = parser.parse_args()
	link=args.Link
	load_dotenv()
	token = os.environ['BITLY_TOKEN']
	if is_bitlink(token,link):
		print (f'Колличество кликов:{count_clicks(token, link)}')
	else:
		print (f'Короткая ссылка: {shorten_link(token, link)}')

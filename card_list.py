import json
import argparse

json_file = 'D:\yugioh-db\card_list.json'

parser = argparse.ArgumentParser(description='A script to track Yu-Gi-Oh! cards.')
parser.add_argument('--attributes', help='attributes of card you\'re performing operations on.')
parser.add_argument('--add', help='Add an owned card to tracking.')
parser.add_argument('--card_num', help='Card number of the card you\'re performing operations on.')
parser.add_argument('--goes_with', help='List of cards a particular card is related to.')
parser.add_argument('--name', help='Name of card you\'re performing operations on.')
parser.add_argument('--quantity', help='Quantity of specific card.')
parser.add_argument('--type', help='Type of card you\'re performing operations on (spell, monster, trap).')
args = parser.parse_args()

# Open current list
with open(json_file, 'r') as data:
    cardList = json.load(data)

# Add card to list
name = args.name
attributes = args.attributes
card_num = args.card_num
quantity = args.quantity
type = args.type

cardList[name] = {}
cardList[name]['Attributes'] = attributes
cardList[name]['Quantity'] = quantity
cardList[name]['Card_Num'] = card_num
cardList[name]['Type'] = type
cardList[name]['Goes_With'] = []

# Overwrite old list with new addittions
with open(json_file, 'w') as data:
    json.dump(cardList, data)

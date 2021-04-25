from trello import TrelloClient
import json

with open('credentials.json', 'r') as creds_file:
    creds = json.load(creds_file)

client = TrelloClient( creds['api_key'], creds['api_secret'], creds['user_token'], creds['user_secret'])

for board in client.list_boards():
    if board.name == 'book':
        book_board = board

for list in board.list_lists():
    if list.name == 'unsorted chapters':
        unsorted_list = list

with open('writing.json', 'r') as writing_file:
    writing_list = json.load(writing_file)

def format_description(article):
    return article['url'] + '\n' + article['description'] + '\n' + '\n'.join(article['tags'])

for article in writing_list:
    card = unsorted_list.add_card(article['name'], format_description(article))
    print(f"added {card.name}")

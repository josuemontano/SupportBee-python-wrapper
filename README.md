# SupportBee API python wrapper
A Python wrapper around the SupportBee API. Please refer to [the official API docs](developers.supportbee.com/api) for details about its API. This project was developed as part of SupportBee's hiring process, one of the best I've ever seen.

### Fetch tickets

You can use all the parametes defined in the [documentation](https://developers.supportbee.com/api#fetching_tickets) as long as they are named exactly the same as in the docs.

```python
from supportbee.client.tickets import TicketsClient

# Fetch collection of tickets
client = TicketsClient(company='your_company', api_token='your_api_token')
tickets = client.get_collection()
tickets = client.get_collection(per_page=5, page=2)
tickets = client.get_collection(archived=True)
```

### Run tests

Tests are written with pytest. Just run `<VENV>/bin/py.test` from console.

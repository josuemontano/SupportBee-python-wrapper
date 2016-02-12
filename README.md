# SupportBee API python wrapper
A Python wrapper around the SupportBee API. Please refer to [the official API docs](developers.supportbee.com/api) for details about its API. This project was developed as part of SupportBee's hiring process, one of the best I've ever seen.

### Fetch tickets

```python
from supportbee.client.tickets import TicketsClient

# Fetch collection of tickets
client = TicketsClient(company='your_company', api_token='your_api_token')
tickets = client.get()
```

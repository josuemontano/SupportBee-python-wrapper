from marshmallow import Schema, fields
from marshmallow.decorators import post_load, pre_load

from .models import Ticket, Requester


class RequesterSchema(Schema):
    name = fields.String()
    email = fields.String()

    @post_load
    def make_object(self, data):
        return Requester(**data)


class TicketSchema(Schema):
    id = fields.Integer()
    subject = fields.String()
    content = fields.String()
    requester = fields.Nested(RequesterSchema, load_only=True)
    requester_name = fields.Function(lambda obj: obj.requester.name, dump_only=True)
    requester_email = fields.Function(lambda obj: obj.requester.email, dump_only=True)

    @post_load
    def make_object(self, data):
        return Ticket(**data)

    @pre_load
    def build_requester(self, in_data):
        in_data['requester'] = dict(name=in_data['requester_name'], email=in_data['requester_email'])
        return in_data

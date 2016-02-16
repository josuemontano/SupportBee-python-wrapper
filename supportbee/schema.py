from marshmallow import Schema, fields
from marshmallow.decorators import post_load, pre_load

from .models import Ticket, Requester


class RequesterSchema(Schema):
    __model__ = Requester

    name = fields.String()
    email = fields.Email()

    @post_load
    def make_object(self, data):
        return self.__model__(**data)


class TicketSchema(Schema):
    __model__ = Ticket

    id = fields.Integer()
    subject = fields.String()
    content = fields.Dict()
    summary = fields.String()

    spam = fields.Boolean()
    starred = fields.Boolean()
    unanswered = fields.Boolean()
    archived = fields.Boolean()

    replies_count = fields.Integer()
    comments_count = fields.Integer()

    requester = fields.Nested(RequesterSchema, load_only=True)
    requester_name = fields.Function(lambda obj: obj.requester.name, dump_only=True)
    requester_email = fields.Function(lambda obj: obj.requester.email, dump_only=True)

    @post_load
    def make_object(self, data):
        return self.__model__(**data)

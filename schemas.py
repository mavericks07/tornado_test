from marshmallow import Schema, fields


class UserSchema(Schema):

    class Meta:
        fields = ("id", "username",)

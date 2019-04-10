
class IntrospectionDisabledException(Exception):
    pass

class DisableIntrospectionMiddleware(object):
    def resolve(self, next, root, info, **kwargs):
        if info.field_name.lower() in ['__schema', '__introspection']:
            raise IntrospectionDisabledException
        return next(root, info, **kwargs)


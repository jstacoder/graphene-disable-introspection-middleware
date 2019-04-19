wish you could turn off `graphene_djangos` introspection abilities? 

now you can:

`GraphqlView.as_view(middleware=[DisableIntrospectionMiddleware()])` and its off

or if your testing, just pass the `middleware` argument to your execute calls:

`graphql_client.execute(query, middleware=[DisableIntrospectionMiddleware()])`

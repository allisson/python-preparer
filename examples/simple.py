import pprint

from preparer import FieldsPreparer

pp = pprint.PrettyPrinter(indent=4)
payload = {
    'type': 'articles',
    'id': '1',
    'attributes': {
        'title': 'JSON API paints my bikeshed!',
        'body': 'The shortest article. Ever.',
        'created': '2015-05-22T14:56:29.000Z',
        'updated': '2015-05-22T14:56:28.000Z'
    },
    'relationships': {
        'author': {
            'data': {'id': '42', 'type': 'people'}
        }
    },
    'tags': [
        {'name': 'tag-1', 'count': 1},
        {'name': 'tag-2', 'count': 2},
        {'name': 'tag-3', 'count': 3},
    ],
}

preparer = FieldsPreparer(fields={
    'id': 'id',
    'type': 'type',
    'title': 'attributes.title',
    'body': 'attributes.body'
})

pp.pprint(preparer.prepare(payload))

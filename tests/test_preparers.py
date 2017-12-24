from simple_model.builder import model_builder


def test_simple_preparer_lookup_data_with_dict(simple_preparer, payload):
    assert simple_preparer.lookup_data('', payload) == payload
    assert simple_preparer.lookup_data('type', payload) == payload['type']
    assert simple_preparer.lookup_data('attributes.title', payload) == payload['attributes']['title']
    assert simple_preparer.lookup_data('relationships.author.data.id', payload) == payload['relationships']['author']['data']['id']


def test_simple_preparer_lookup_data_with_object(simple_preparer, payload):
    obj = model_builder(payload)
    assert simple_preparer.lookup_data('', obj) == obj
    assert simple_preparer.lookup_data('type', obj) == obj.type
    assert simple_preparer.lookup_data('attributes.title', obj) == obj.attributes.title
    assert simple_preparer.lookup_data('relationships.author.data.id', obj) == obj.relationships.author.data.id


def test_simple_preparer_prepare(simple_preparer, payload):
    expected = {
        'type': 'articles',
        'id': '1',
        'title': 'JSON API paints my bikeshed!',
        'body': 'The shortest article. Ever.',
        'relationship_id': '42'
    }
    assert simple_preparer.prepare(payload) == expected
    assert simple_preparer.prepare(model_builder(payload)) == expected


def test_simple_preparer_without_fields_prepare(simple_preparer_without_fields, payload):
    assert simple_preparer_without_fields.prepare(payload) == payload
    assert simple_preparer_without_fields.prepare(model_builder(payload)) == payload


def test_preparer_with_subpreparer_prepare(preparer_with_subpreparer, payload):
    expected = {
        'type': 'articles',
        'id': '1',
        'attrs': {
            'title': 'JSON API paints my bikeshed!',
            'body': 'The shortest article. Ever.'
        }
    }
    assert preparer_with_subpreparer.prepare(payload) == expected
    assert preparer_with_subpreparer.prepare(model_builder(payload)) == expected


def test_preparer_with_collectionsubpreparer_prepare(preparer_with_collectionsubpreparer, payload):
    expected = {
        'type': 'articles',
        'id': '1',
        'tag_list': [
            {'tag_name': 'tag-1'},
            {'tag_name': 'tag-2'},
            {'tag_name': 'tag-3'},
        ]
    }
    assert preparer_with_collectionsubpreparer.prepare(payload) == expected
    assert preparer_with_collectionsubpreparer.prepare(model_builder(payload)) == expected

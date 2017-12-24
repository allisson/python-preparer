import pytest

from preparer import CollectionSubPreparer, FieldsPreparer, SubPreparer


@pytest.fixture
def payload():
    return {
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


@pytest.fixture
def simple_preparer_without_fields():
    return FieldsPreparer()


@pytest.fixture
def simple_preparer():
    fields = {
        'type': 'type',
        'id': 'id',
        'title': 'attributes.title',
        'body': 'attributes.body',
        'relationship_id': 'relationships.author.data.id'
    }
    return FieldsPreparer(fields=fields)


@pytest.fixture
def preparer_with_subpreparer():
    attributes_preparer = FieldsPreparer(
        fields={'title': 'title', 'body': 'body'}
    )
    fields = {
        'type': 'type',
        'id': 'id',
        'attrs': SubPreparer('attributes', attributes_preparer)
    }
    return FieldsPreparer(fields=fields)


@pytest.fixture
def preparer_with_collectionsubpreparer():
    tags_preparer = FieldsPreparer(fields={'tag_name': 'name'})
    fields = {
        'type': 'type',
        'id': 'id',
        'tag_list': CollectionSubPreparer('tags', tags_preparer)
    }
    return FieldsPreparer(fields=fields)

import pprint

from preparer import FieldsPreparer, SubPreparer, CollectionSubPreparer


pp = pprint.PrettyPrinter(indent=4)
xfiles_game = {
    'description': 'As an extension of one of the most long-running...',
    'game_id': 1,
    'genres': [
        {
            'genre_category': 'Basic Genres',
            'genre_category_id': 1,
            'genre_id': 2,
            'genre_name': 'Adventure'
        },
        {
            'genre_category': 'Perspective',
            'genre_category_id': 2,
            'genre_id': 7,
            'genre_name': '1st-person'
        },
        {
            'genre_category': 'Narrative Theme/Topic',
            'genre_category_id': 8,
            'genre_id': 55,
            'genre_name': 'Detective / Mystery'
        },
        {
            'genre_category': 'Setting',
            'genre_category_id': 10,
            'genre_id': 8,
            'genre_name': 'Sci-Fi / Futuristic'
        },
        {
            'genre_category': 'Other Attributes',
            'genre_category_id': 6,
            'genre_id': 82,
            'genre_name': 'Licensed Title'
        }
    ],
    'moby_score': 3.8,
    'moby_url': 'http://www.mobygames.com/game/x-files-game',
    'num_votes': 53,
    'official_url': None,
    'platforms': [
        {
            'first_release_date': '1998',
            'platform_id': 3,
            'platform_name': 'Windows'
        },
        {
            'first_release_date': '1998-06',
            'platform_id': 74,
            'platform_name': 'Macintosh'
        },
        {
            'first_release_date': '1999',
            'platform_id': 6,
            'platform_name': 'PlayStation'
        }
    ],
    'sample_cover': {
        'height': 927,
        'image': 'http://www.mobygames.com/images/covers/l/3-the-x-files-game...',
        'platforms': [
            'Windows'
        ],
        'thumbnail_image': 'http://www.mobygames.com/images/covers/s/3-the-x-files...',
        'width': 800
    },
    'sample_screenshots': [
        {
            'caption': 'Mulder and Special Agent Willmore',
            'height': 480,
            'image': 'http://www.mobygames.com/images/shots/l/86087-the-x-files...',
            'thumbnail_image': 'http://www.mobygames.com/images/shots/s/86087-the...',
            'width': 640
        },
        {
            'caption': 'Title screen (from intro)',
            'height': 480,
            'image': 'http://www.mobygames.com/images/shots/l/313897-the-x-files-game...',
            'thumbnail_image': 'http://www.mobygames.com/images/shots/s/313897-the-x...',
            'width': 640
        },
        {
            'caption': 'Gillian Anderson (from intro)',
            'height': 480,
            'image': 'http://www.mobygames.com/images/shots/l/313919-the-x-files-game...',
            'thumbnail_image': 'http://www.mobygames.com/images/shots/s/313919-the-x...',
            'width': 640
        },
        {
            'caption': 'David Duchovny (from intro)',
            'height': 480,
            'image': 'http://www.mobygames.com/images/shots/l/313908-the-x-files-game-windows...',
            'thumbnail_image': 'http://www.mobygames.com/images/shots/s/313908-the-x-files...',
            'width': 640
        }
    ],
    'title': 'The X-Files Game'
}

preparer = FieldsPreparer(fields={
    'id': 'game_id',
    'title': 'title',
    'description': 'description'
})

cover_preparer = FieldsPreparer(fields={
    'image': 'image',
    'thumbnail': 'thumbnail_image'
})
preparer_with_cover = FieldsPreparer(fields={
    'id': 'game_id',
    'title': 'title',
    'description': 'description',
    'cover': SubPreparer('sample_cover', cover_preparer)
})

screenshot_preparer = FieldsPreparer(fields={
    'caption': 'caption',
    'image': 'image',
    'thumbnail': 'thumbnail_image'
})
preparer_with_cover_and_screenshot = FieldsPreparer(fields={
    'id': 'game_id',
    'title': 'title',
    'description': 'description',
    'cover': SubPreparer('sample_cover', cover_preparer),
    'screenshots': CollectionSubPreparer('sample_screenshots', screenshot_preparer)
})

pp.pprint(preparer.prepare(xfiles_game))
pp.pprint(preparer_with_cover.prepare(xfiles_game))
pp.pprint(preparer_with_cover_and_screenshot.prepare(xfiles_game))

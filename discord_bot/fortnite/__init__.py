def landing_spots(season: int, chapter: int):

    spots = {
        4: {
            2: [
                'Anvil Square',
                'Breakwater Bay',
                'Frenzy Fields',
                'Steamy Springs',
                'Shattered Slabs',
                'Mega City',
                'Kenjutsu Crossing',
                'Knotty Nets',
                'Brutal Bastion',
                'Lonely Labs',
                'Slappy Shores',
                'The Citadel'
            ]
        }
    }

    try:
        return spots[season][chapter]
    except KeyError as e:
        return None

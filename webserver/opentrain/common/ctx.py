def menu(req):
    menu_items = [#dict(title="Search Between",name = 'gtfs:search-between'),
                  dict(title="Search In",name = 'gtfs:search-in'),
                  dict(title="Show labels",name = 'analysis:show-labels'),
                  dict(title="Show Reports",name = 'analysis:select-device-reports')
                  ]
    for mi in menu_items:
        mi['active'] = False
    return dict(menu_items = menu_items)



    
    
    

__author__ = 'grijesh'


# ALL_ITEM_QUERY = "select mi.item_id,mi.item_name,mb.brand_name
# ,mc1.category_name as sub_category ,mc2.category_name " \
#                 "from market_item mi,market_category mc1, market_category mc2,market_brand mb,auth_user au " \
#                 "where mi.sub_category_id = mc1.category_id and mc1.parent_id = mc2.category_id " \
#                 "and mi.brand_id = mb.brand_id and au.username = mi.username_id"

ALL_ITEM_QUERY = 'select mi.item_id,mi.item_name,mb.brand_name,mc1.category_name as sub_category,' \
                 'mc2.category_name,mi.price,mi.qty,au.username as seller ' \
                 'from market_item mi,market_categorymst mc1, market_categorymst mc2,market_brand mb,auth_user au ' \
                 'left join market_disabledcategories md on md.username_id = au.username  ' \
                 'where mi.sub_category_id = mc1.category_id and mc1.parent_id = mc2.category_id ' \
                 'and mi.brand_id = mb.brand_id and au.username = mi.username_id ' \
                 'and (md.category_id is null OR mc2.category_id <> md.category_id)'

BRAND_QUERY = 'select brand_id,brand_name from market_brand'

DISABLE_CATEGORY = 'Insert into market_disabledcategories(category_id,username_id) values (%s,%s)'

ENABLE_CATEGORY = 'Delete from market_disabledcategories where username_id = %s and category_id = %s'

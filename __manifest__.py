{
    'name': 'MashiJai Shipping',
    'version': '17.0.1.0.1',
    'category': 'Inventory/Delivery',
    'summary': 'Peer-to-peer shipping management',
    'description': """
MashiJai Shipping
=================
A peer-to-peer shipping platform that connects travelers with excess luggage space
to customers who need to ship items along the same route.

Features:
- Trip management for travelers
- Booking management for customers
- Searchable homepage with form and listings
- Rating system for bookings
- Portal integration with custom pages and menu items
""",
    'author': 'webTronex Technologies',
    'website': 'https://www.webTronex.ca',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': [
        'base',
        'mail',
        'portal',
        'web',
        'website',
    ],
    'data': [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',

        # Configuration & Data
        'data/res.config.xml',
        'data/ir_sequence.xml',
        'data/ir_cron.xml',
        'data/mail_templates.xml',
        'data/shipping_cron.xml',

        # Website & Portal pages
        'views/website_templates.xml',
        'views/portal_buttons.xml',
        'views/portal_dashboard.xml',
        'views/portal_traveler_access.xml',
        'views/portal_customer_dashboard.xml',
        'views/portal_my_bookings.xml',
        'views/portal_traveler_dashboard.xml',
        'views/portal_booking_form.xml',
        'views/portal_new_listing.xml',
        'views/search_results.xml',
        'views/extended_search_listings.xml',
        'views/public_shipping_listings.xml',
        'views/manage_listings.xml',
        'views/my_shipping_bookings.xml',
        'views/booking_detail.xml',
        'views/rate_user.xml',
        'views/rate_traveler.xml',
        'views/trip_details.xml',
        'views/create_trip_form.xml',
        'views/menus.xml',
        'views/trip_views.xml',
        'views/booking_views.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
}
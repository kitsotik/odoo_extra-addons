{
    'name': 'Sale Order Custom Price',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Retain custom price in sale order lines when applying pricelists',
    'description': """
        This module ensures that when a sale order line has a custom price,
        this price is retained even when changing pricelists in the POS.
    """,
    'author': 'kitsotik',
    'depends': ['sale', 'point_of_sale'],
    'data': [
        # No XML data files are required for this functionality
    ],
    'installable': True,
    'application': False,
}

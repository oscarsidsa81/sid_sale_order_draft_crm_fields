{
    'name': 'sid_sale_order_draft_crm_fields',
    'version': '1.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Campos en vista tree y form relacionados con el CRM',
    'description': 'Campos para la identificación de la oportunidad vinculada a los diferentes presupuestos',
    'author': 'oscarsidsa81',
    'depends': ['base','sale_management','crm','oct_sale_extra_fields'],
    'data': [
        'views/sid_sale_order_draft_crm_fields.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
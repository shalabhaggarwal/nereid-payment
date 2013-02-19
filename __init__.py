# -*- coding: utf-8 -*-
'''

    Nereid Payment Gateway

    :copyright: (c) 2010-2013 by Openlabs Technologies & Consulting (P) Ltd.
    :license: GPLv3, see LICENSE for more details

'''
from trytond.pool import Pool

from .gateway import *
from .defaults import *
from .register import *


def register():
    Pool.register(
        PaymentGateway,
        DefaultCheckout,
        PaymentGatewayCountry,
        WebSite,
        PaymentGatewayWebsite,
        PaymentGatewaySale,
        COD,
        Cheque,
        Register,
        RegisterLog,
        Invoice,
        type_="model", module="nereid_payment"
    )

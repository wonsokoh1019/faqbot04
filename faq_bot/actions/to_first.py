# !/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import logging
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.externals.send_message import push_message
import gettext
_ = gettext.gettext


@tornado.gen.coroutine
def to_first(account_id, __, ___):
    process_flag = False
    if process_flag:
        fmt = _("Cannot be selected since you are currently in Initial Menu. \n\n"
                "Select it if you want to find FAQ or go back to Initial Menu "
                "while the person in charge is checking your question.")
        content = make_i18n_text("Cannot be selected since you are currently "
                            "in Initial Menu. \n\n"
                            "Select it if you want to find FAQ or go back to "
                            "Initial Menu while the person in charge is "
                            "checking your question.", "to_first", fmt)
    else:
        fmt = _("Moved to FAQ Initial Menu.")
        content = make_i18n_text("Moved to FAQ Initial Menu.", "to_first", fmt)

    yield push_message(account_id, content)
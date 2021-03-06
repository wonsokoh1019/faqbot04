# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deals with user query security related problems.
"""

__all__ = ['query_security']

import tornado.gen
import tornado.web
import logging
from conf.resource import CAROUSEL, POST_BACK_URLS
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.actions.message import create_quick_replay_item, create_carousel
from faq_bot.externals.send_message import push_messages
import gettext
_ = gettext.gettext

@tornado.gen.coroutine
def query_security(account_id, __, ___):
    """
    This function deals with user query security related problems.

    :param account_id: user account id.
    """
    fmt = _("Here are FAQs about security.")
    text = make_i18n_text("Here are FAQs about security.", "query_security", fmt)

    fmt = _("Send a question")
    replay = create_quick_replay_item("transfer_security", "query_security",
                                      "Send a question", fmt)

    labels = ["See more", "See more", "See more", "See more"]

    fmt = _("See more")
    i18n_label_fmts = [fmt, fmt, fmt, fmt]

    titles = [
        "I lost my access card.",
        "My access card has been damaged.",
        "Can visitors enter the office?",
        "I can’t remember my computer password."
    ]
    
    i18n_title_fmts = [
        _("I lost my access card."),
        _("My access card has been damaged."),
        _("Can visitors enter the office?"),
        _("I con’t remember my computer password.")
    ]
    texts = [
        "Contact the Security Team to reissue your access card.",
        "Contact the Security Team to reissue your access card.",
        "Contact the Security Team in advance to gain access.",
        "Contact the Security Team to change your computer password."
    ]

    fmt = _("Contact the Security Team to reissue your access card.")
    i18n_text_fmts = [
        fmt,
        fmt,
        _("Contact the Security Team in advance to gain access."),
        _("Contact the Security Team to change your computer password.")
    ]

    carousel = create_carousel("query_security", labels,
                               POST_BACK_URLS["security"], texts, titles,
                               CAROUSEL["security"],
                               fmt_labels=i18n_label_fmts,
                               fmt_texts=i18n_text_fmts,
                               fmt_titles=i18n_title_fmts)

    carousel["quickReply"] = replay

    yield push_messages(account_id, [text, carousel])


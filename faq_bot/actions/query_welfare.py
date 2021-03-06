# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deals with user query welfare related problems
"""

__all__ = ['query_welfare']

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
def query_welfare(account_id, __, ___):
    """
    This function deals with user query welfare related problems.

    :param account_id: user account id.
    """
    fmt = _("Here are FAQs about welfare and work support.")
    text = make_i18n_text("Here are FAQs about welfare and work support.",
                          "query_welfare", fmt)

    fmt = _("Send a question")
    replay = create_quick_replay_item("transfer_welfare",  "query_welfare",
                                      "Send a question", fmt)

    labels = ["See more", "See more", "See more", "See more"]

    fmt = _("See more")
    i18n_label_fmts = [fmt, fmt, fmt, fmt]

    titles = [
        "The types of in-house welfare.",
        "What kinds of in-house clubs are there?",
        "Can I use a company car?",
        "How can I receive office supplies?"
    ]

    i18n_title_fmts = [
        _("The types of in-house welfare."),
        _("What kinds of in-house clubs are there?"),
        _("Can I use a company car?"),
        _("How can I receive office supplies?")
    ]

    texts = [
        "Welfare includes the four main insurances, checkup, etc.",
        "A variety of club activities such as sports are supported.",
        "Contact the Work Support Team to request a company car.",
        "Visit the Work Support Team to receive office supplies."
    ]

    i18n_text_fmts = [
        _("Welfare includes the four main insurances, checkup, etc."),
        _("A variety of club activities such as sports are supported."),
        _("Contact the Work Support Team to request a company car."),
        _("Visit the Work Support Team to receive office supplies.")
    ]

    carousel = create_carousel("query_welfare", labels, POST_BACK_URLS["welfare"],
                               texts, titles, CAROUSEL["welfare"],
                               fmt_labels=i18n_label_fmts,
                               fmt_texts=i18n_text_fmts,
                               fmt_titles=i18n_title_fmts)

    carousel["quickReply"] = replay

    yield push_messages(account_id, [text, carousel])
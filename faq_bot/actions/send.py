# !/bin/env python
# -*- coding: utf-8 -*-
"""
Process user confirmation message content
"""
import tornado.web
import tornado.gen
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.constant import TYPES
from faq_bot.actions.message import create_quick_replay
from faq_bot.externals.send_message import push_messages
from faq_bot.externals.home import create_articles
from faq_bot.model.cachehandle import get_user_status, clean_user_status
import gettext
_ = gettext.gettext


@tornado.gen.coroutine
def send(account_id, __, ___):
    """
    This function processes the content of the user confirmation message

    :param account_id: user account.
    """
    status, __, type, message = get_user_status(account_id)
    if status != "done" or message is None:
        # todo add error prompt
        raise HTTPError(500, "user status error. status error")

    fmt = _("Your question has been sent to the person in charge. \n\n"
            "The staff will answer your question as soon as possible.")
    content = make_i18n_text(
        "Your question has been sent to the person in charge. \n\n"
        "The staff will answer your question as soon as possible.",
        "send", fmt)

    fmt = _("If you have any additional questions, "
            "please select the task from below. "
            "If you want to go back to the initial stage, "
            "select [Go to Initial Menu] from the menu below.")
    content1 = make_i18n_text("If you have any additional questions, "
                              "please select the task from below. "
                              "If you want to go back to the initial stage, "
                              "select [Go to Initial Menu] from the menu below.",
                              "send", fmt)

    content1["quickReply"] = create_quick_replay()

    title = "{type} inquiry details".format(type=TYPES[type])
    prompt_message = yield create_articles(title, type, message, account_id)
    if prompt_message is not None:
        yield push_messages(account_id, [prompt_message])
        return

    clean_user_status(account_id)
    yield push_messages(account_id, [content, content1])
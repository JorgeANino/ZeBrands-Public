from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from user.models import CatalogUser


def send_updated_product_email(product):
    """Sends an email to all admins referring to an updated product"""
    mail_subject = "Catalog System: a product has been updated"
    message_plain = render_to_string(
        settings.UPDATE_PRODUCT_EMAIL_MAIL_PLAIN,
        {
            "product": product,
        },
    )
    message_html = render_to_string(
        settings.UPDATE_PRODUCT_EMAIL_MAIL_HTML,
        {
            "product": product,
        },
    )

    to_emails = []
    users = CatalogUser.objects.all()
    for user in users:
        to_emails.append(user.email)
    if settings.EMAIL_ADDRESS:
        send_mail(
            mail_subject,
            message_plain,
            settings.EMAIL_ADDRESS,
            to_emails,
            html_message=message_html,
        )

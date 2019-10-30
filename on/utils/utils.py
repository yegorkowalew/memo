from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)

def ind(request):
    logger.info("Page ON admin index with %s user." % (request.user))
    return render(request, 'adm/on-adm-ind.html', {})
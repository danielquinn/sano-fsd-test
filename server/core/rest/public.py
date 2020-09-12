# API for public endpoints
# Note: think carefully before putting anything in here...
# ...anyone will have access to data exposed from these endpoints

import json
import logging
import zlib
from time import sleep, time

import peewee
import stripe
from dateutil.parser import parse
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request

from core.auth.store import auth_store
from core.config import config

logger = logging.getLogger(__name__)
public_api = Blueprint("public_api", __name__)


# -------
# Write you endpoint to retrieve all available studies here.
# -------

__notes = """
And sadly, this is where I decided to give up.  Honestly, this isn't a
reasonable test.

I just spent 2+ hours dockerising this project because I'm not interested in
running some stranger's unvetted codebase on my personal machine.  I had to
work around things like hard-coded secrets, hard-coded URLs, and a codebase
that gleefully boasts about something like 90 known vulnerabilities.

Now I finally get to the "write some code" stage and you've asked for an
endpoint but provided no format for the JSON response and no URL for it either.
It's not clear what's expected here, but for a test at this stage, the options
of (a) digging into the client-side code or (b) guessing,  aren't tasks I'm
going to take on.  I did check the web console though.  No endpoint is
requested when you hit /reseach, so I'm just going to go out on a limb and
assume that I have to make a guess there too.  You want me to do this, and 6
other tasks in 3 hours?

To be honest with you, I'm not a fan of technical tests in general.  They
don't test for critical things like communication skills (we could have done
something like this collaboratively, where I can ask questions rather than be
forced to guess), problem-solving skills, or anything you actually want in a
developer really.  What they do test is whether or not I can pull records from
a database and serialise them... after a lot of guesswork I don't have time
for.  To ask for this kind of investment this early in the process, when the
test is this invasive, this vague in its expectations, and documented in three
different places -- it's a bridge too far.  I've got other work I could be
doing today.

Seriously though, all grumpiness aside, this is a ridiculous test to hand
someone so early in the interview process.  I understand that some people feel
a tech test is a reasonable ask to show investment in a role, but we haven't
even had a conversation yet, and already you've eaten a good chunk of my
Saturday.  Honestly, it's disrespectful.

In the interests of "the campsite rule" (leaving relationships better than how
you found them), I have a few recommendations:

* Don't issue a technical test until you've determined that the candidate in
  question is who/what you want and that they feel the same way about you.
* Consider if a test is even necessary if the candidate has provided ample code
  samples or references.
* If you must issue a technical test, vet it with someone who will give you an
  honest opinion about its value to you as a company:
    * What exactly are you testing for?  Does this test for it?
    * Are your time estimates accurate?  Is that a reasonable imposition?
    * What're the chances that your candidate will be able to run your test on
      on their machine without an overabundance of effort?  For example, this
      test absolutely should have been delivered as a dockerised system.
      Expecting people to run thousands of lines of untrusted code on their
      bare-metal machines is absolutely unreasonable.
* Finally, and I understand that this may seem strange at first, but if you're
  going to ask someone to give up 3+ hours of their life for you, *pay them*.
  They're doing work for you after all.  Even an Amazon gift card for £100 will
  go a long way toward showing them that you have respect for them and their
  time.

That's it for me.  My kid is about to go to sleep, and I'd like to spend some
time with her before she goes to bed.
"""

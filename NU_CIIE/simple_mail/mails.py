from simple_mail.mailer import BaseSimpleMail, simple_mailer


class WelcomeMail(BaseSimpleMail):
    email_key = 'Welcome'

class eventMail1(BaseSimpleMail):
	email_key = 'Event'

class eventMail2(BaseSimpleMail):
	email_key = 'Event2'

class eventMail3(BaseSimpleMail):
	email_key = 'Event3'

class eventMail4(BaseSimpleMail):
	email_key = 'Event4'

class eventMail5(BaseSimpleMail):
	email_key = 'Event5'

class eventMail6(BaseSimpleMail):
	email_key = 'Event6'

simple_mailer.register(WelcomeMail)
simple_mailer.register(eventMail1)
simple_mailer.register(eventMail2)
simple_mailer.register(eventMail3)
simple_mailer.register(eventMail4)
simple_mailer.register(eventMail5)
simple_mailer.register(eventMail6)
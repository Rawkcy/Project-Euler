from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "Do you like me?"
like = raw_input(prompt)
like_me = "do like me."
like_me_not = "You said you do not like me."
print "You said you %s" % like_me if like=="yes" else like_me_not

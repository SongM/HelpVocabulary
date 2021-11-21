from pattern.text.en import conjugate, lemma, lexeme
print (lemma('gave'))
print (lexeme('gave'))


from pattern.text.en import pluralize, singularize

print(pluralize('leaf'))
print(singularize('theives'))
print(singularize('words'))

from pattern.text.en import comparative, superlative

print(comparative('good'))
print(superlative('good'))

from pattern.text.en import suggest

print(suggest("Whitle"))
print(suggest("white"))
print(suggest("assid"))
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Plusserver', 'Dell'])
print(it_companies)

it_companies.remove("Plusserver")
print(it_companies)

# remove() will through an error if the element is not available and discard() will not

print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B.union(A)))

print(A.symmetric_difference(B))

del it_companies
del A
del B

# print(it_companies, A, B)

ageSet = set(age)
print(len(age), len(ageSet))

sentence = 'I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.'

sentenceArray = sentence.split(' ')

print(sentenceArray)

sentenceSet = set(sentenceArray)

print(len(sentenceArray), len(sentenceSet))
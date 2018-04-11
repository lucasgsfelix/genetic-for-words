
import random


#### first genetic algorithm, this was made to learn the specificities of this type of coding
#### this code is for discover a password 
#### based on the article of this website https://blog.sicara.com/getting-started-genetic-algorithms-python-tutorial-81ffa1dd72f9

def fitness(password, testWord): ### this function will return the accuracy of our algorithm
	
	accuracy = 0.0
	if len(password) == len(testWord):

		right = 0.0
		for i in range(0, len(password)):
			if password[i] == testWord[i]:
				right = right + 1

		accuracy = (right/float(len(testWord)))*100.0 #percentual of accuracy

	return accuracy


def generateWord(length):

	#### this function will generate words that will be our individuals
	word = ""
	for i in range(0, length):
		letter = chr(97 + int(26 * random.random())) ### this was take from web to generate random letters
		word = word + letter
	return word


def selectBestLucky(population, bestOnes, luckyOnes): ### we will select a N number of best individuals and M number of luckyOne
	
	population.sort(key=lambda x: x[1], reverse=True)
	populationBest = []
	populationLucky = []
	if (bestOnes + luckyOnes) < len(population):

		for i in range(0, bestOnes): ### selecting population best
			populationBest.append(population[i])
			population.pop(i)

		for i in range(0, luckyOnes): ### selecting population lucky
			value = random.randrange(len(population))
			populationLucky.append(population[value])

	else:

		print "The parameters for bestOnes plus luckyOnes is bigger than the number of individuals in the population !"

	return populationBest, populationLucky

def creatingAChild(best, lucky, numberOfChilds, password): ### This is  "I'm pregnant" code version

	breeders = best + lucky
	nextPopulation = []

	for i in range(0, len(breeders)/2):
		for j in range(0, numberOfChilds):
			nextPopulation.append(makingAChild(breeders[i][0], breeders[len(breeders) -1 -i][0]))

	nextPopulation = fitOfPopulation(nextPopulation, password)
	nextPopulation.sort(key=lambda x: x[1], reverse=True)
	return nextPopulation

def makingAChild(fatherOne, fatherTwo): ### this is the best part of the process
	
	### Lucky I'm your father
	kiddo = ""

	for i in range(0, len(fatherOne)):

		### the first half it's from the fatherOne
		### the other half it's from the fatherTwo
		### We can't deny that is the father face

		if(random.randrange(100)>49): ## this is fatherTwo properties
			kiddo = kiddo + fatherTwo[i]
		else: ## fatherOne 
			kiddo = kiddo + fatherOne[i]

	return kiddo


def fitOfPopulation(population, password):
	accuracyPopulation = []
	j=0
	for i in population:
		accuracyPopulation.append(i) #### we have definide the accuracy for each individual
		accuracyPopulation.append('\t')
		accuracyPopulation.append(str(fitness(password, i)))
		accuracyPopulation.append('\n')
		j=j+1

	accuracyPopulation = ''.join(accuracyPopulation).split('\n')
	for i in range(0, len(accuracyPopulation)):
		accuracyPopulation[i] = accuracyPopulation[i].split('\t')
	accuracyPopulation.pop(len(accuracyPopulation)-1)

	return accuracyPopulation

if __name__ == '__main__':


	password = "password" ### the word that the algorithm will try to discover
	testWord = "alksmdlm"
	accuracy = fitness(password, testWord) ### to initiate the algorithm we give a test word, to give a initial accuracy
	numberOfIndividuals = 100
	
	flag=0
	while(1):
		population = []
		### now we will generate our first population
		for i in range(numberOfIndividuals):
			population.append(generateWord(len(password)))
			
		### now we have our population definide, we have to define the fitness value for each one
		accuracyPopulation = fitOfPopulation(population, password)

		best, lucky = selectBestLucky(accuracyPopulation, 50, 10) ### these are random parameters

		### and now we have the best and lucky breeders

		population = creatingAChild(best, lucky, 10, password) ## arbitrary number of childs

		for i in range(0, len(population)):
			if float(population[i][1])>=40:
				print population[i]
				flag=1
		
		if flag==1:
			break




	



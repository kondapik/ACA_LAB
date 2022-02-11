import os, re, json
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
# import numpy as np

def readOutput(tParams, consolidatedResults):
    oFile = open(outputFile)
    if oFile:
        regex = r"Writes:\s(?P<writes>\d*)\s*Write Misses:\s(?P<wMisses>\d*)\s*Reads:\s(?P<reads>\d*)\s*Read Misses:\s(?P<rMisses>\d*)\s*Misses:\s(?P<misses>\d*)\s*Accesses:\s(?P<accesses>\d*)\s*Miss Ratio:\s(?P<mRatio>[\d.%]*)"
        matches = re.search(regex, oFile.read())
        if matches:
            consolidatedResults.append({'cacheSize':tParams[0],'blockSize':tParams[1], 'associativity':tParams[2], 'writes':matches.group('writes'), 'writeMisses':matches.group('wMisses'),
                                        'misses':matches.group('misses'), 'accesses':matches.group('accesses'), 'missRatio':matches.group('mRatio')})
        else:
            print('Error: didnt find the results in the output file')

        oFile.close()
    else:
        print('Error: Cannot read the output file')

def myplot(consolidatedResults, marker):
    plt.plot([data['years'] for data in monthMeans],
             [data['temp'] for data in monthMeans],
             marker)

outputFile = 'avdc.out'
shellFile = 'pin-avdc.sh'
programPath = '../radix/radix'

consolidatedResults = [] #a list of dictionaries to record data of all runs

# list to contain parameters to test cache - [[Size(B), Block Size(B), Associativity]]
testingParameters = [[16384, 16, 1],
                    [16384, 16, 2],
                    [16384, 32, 1],
                    [16384, 32, 2],
                    [16384, 64, 1],
                    [16384, 64, 2],
                    [32768, 16, 1],
                    [32768, 32, 1],
                    [32768, 64, 1],
                    [32768, 16, 2],
                    [32768, 32, 2],
                    [32768, 64, 2],
                    [65536, 16, 1],
                    [65536, 16, 2],
                    [65536, 32, 1],
                    [65536, 32, 2],
                    [65536, 64, 1],
                    [65536, 64, 2]]

for tParams in testingParameters:
    os.system('./' + shellFile + ' -s ' + str(tParams[0]) + ' -l ' + str(tParams[1]) + ' -a ' + str(tParams[2]) + ' -- ' + programPath + ' -n 100000')
    readOutput(tParams, consolidatedResults)

outfile = open('json_data.json', 'w')
print(json.dumps(consolidatedResults, indent=4))
json.dump(consolidatedResults,outfile,indent=4)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# width = depth = np.ones(len(consolidatedResults))
# bottom = np.zeros(len(consolidatedResults))

# ax.bar3d({data['cacheSize'] for data in consolidatedResults}, {data['cacheSize'] for data in consolidatedResults})


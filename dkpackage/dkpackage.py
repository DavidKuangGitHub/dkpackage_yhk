'''dkpackage.py'''
'''Last Updated: May 14th Thu 2020'''


class Davidsolution(object):
    def start(self, strs):
        return strs + "[thread:START]"

    def stop(self, strs):
        return strs + "[thread:STOP]"


'''myDavidSolution = Davidsolution()
print(myDavidSolution.start("DKpackage: Started!")+" and "+myDavidSolution.stop("DKpackage: Stopped!"))'''

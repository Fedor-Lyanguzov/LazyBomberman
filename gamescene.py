#!/usr/bin/python3
"""
Template for new module
"""

from cocos.director import director

def main():
    """ Test scene """
    director.init(width=800, height=600, autoscale=True)
    director.run(Intro())
    

if __name__ == "__main__":
    main()

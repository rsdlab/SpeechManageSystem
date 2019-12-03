#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SpeechProvider_idl_examplefile.py
 @brief Python example implementations generated from SpeechProvider.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import Provider, Provider__POA
import time

class SpeechProvider_i (Provider__POA.SpeechProvider):
        
    """
    @class SpeechProvider_i
    Example class implementing IDL interface Provider.SpeechProvider
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        self.m_speechdata = ""
        self.sleeptime = 0
        self.Flag = 0
        
        pass

    # void read(in string speechcontents)
    def read(self, speechcontents):
        self.m_speechdata = speechcontents
        self.sleeptime = len(speechcontents)/14
        self.Flag = 1
        #raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = SpeechProvider_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()


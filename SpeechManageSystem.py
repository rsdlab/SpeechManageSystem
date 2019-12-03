#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SpeechManageSystem.py
 @brief SpeechManageSystem
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import SpeechProvider_idl
import SpeechConsumer_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from SpeechProvider_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import Provider, Provider__POA
import Consumer, Consumer__POA


# </rtc-template>

speechstate = ""
startFlag = 0

# This module's spesification
# <rtc-template block="module_spec">
speechmanagesystem_spec = ["implementation_id", "SpeechManageSystem", 
		 "type_name",         "SpeechManageSystem", 
		 "description",       "SpeechManageSystem", 
		 "version",           "1.0.0", 
		 "vendor",            "hiroyasu_tsuji", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class SpeechManageSystem
# @brief SpeechManageSystem
# 
# 
class SpeechManageSystem(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_speechout = RTC.TimedString(RTC.Time(0,0),"")
		"""
		"""
		self._speechoutOut = OpenRTM_aist.OutPort("speechout", self._d_speechout)

		"""
		"""
		self._speechinPort = OpenRTM_aist.CorbaPort("speechin")
		"""
		"""
		self._speechstatePort = OpenRTM_aist.CorbaPort("speechstate")

		"""
		"""
		self._SpeechProviderProvider = SpeechProvider_i()
		

		"""
		"""
		self._SpeechConsumerRequire = OpenRTM_aist.CorbaConsumer(interfaceType=Consumer.SpeechConsumer)
                self.StartFlag = 0

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		self.addOutPort("speechout",self._speechoutOut)
		
		# Set service provider to Ports
		self._speechinPort.registerProvider("SpeechProvider", "Provider::SpeechProvider", self._SpeechProviderProvider)
		
		# Set service consumers to Ports
		self._speechstatePort.registerConsumer("SpeechConsumer", "Consumer::SpeechConsumer", self._SpeechConsumerRequire)
		
		# Set CORBA Service Ports
		self.addPort(self._speechinPort)
		self.addPort(self._speechstatePort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
                self.StartFlag = 1
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
                time.sleep(1)
                if self.StartFlag == 1:
                        self._SpeechConsumerRequire._ptr().write("speechstart")
                        print("SpeechStateStart")
                        self.StartFlag = 0
                
                if self._SpeechProviderProvider.Flag == 1:
                        self._d_speechout.data = self._SpeechProviderProvider.m_speechdata
                        print( "SpeechOutdata : " +  self._d_speechout.data)
                        self._speechoutOut.write()
                        time.sleep(self._SpeechProviderProvider.sleeptime)
                        self._SpeechConsumerRequire._ptr().write("speechend")
                        self._SpeechProviderProvider.Flag = 0
                else :
                        return RTC.RTC_OK
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def SpeechManageSystemInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=speechmanagesystem_spec)
    manager.registerFactory(profile,
                            SpeechManageSystem,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SpeechManageSystemInit(manager)

    # Create a component
    comp = manager.createComponent("SpeechManageSystem")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()


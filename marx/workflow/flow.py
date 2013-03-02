'''
Created on Feb 23, 2013

@author: nino
'''
from marx.workflow.exceptions import Abort
import sys

class Workflow(object):
    def __init__(self, 
                 steps, 
                 on_error=None, 
                 on_abort=None,
                 on_reply=None):
        self.steps = steps
        self.on_error = on_error or self.default_on_error
        self.on_abort = on_abort or self.default_on_abort
        self.reply = on_reply or self.default_on_reply
        
    def __call__(self, context):
        context.workflow = self
        try:
            for step in self.steps:
                try:
                    step(context=context)
                except Abort, e:
                    self.on_abort(context)
                    break
            return context
        except Exception, e:
            return self.on_error(e, context)
                
    def default_on_error(self, e, context):
        raise type(e), e.message, sys.exc_info()[2]
    
    def default_on_abort(self, context):
        pass
    
    def default_on_reply(self, reply, context):
        pass
import logging
class RxTester() : 
    def __init__(self):
        logging.debug("rxTester created")
        self.listener_onnext = [lambda value : logging.debug("-- value on_next   %s" % len(str(value)))] 
        self.listener_onerror = [lambda err : logging.debug(f'--- error occured %s' % str(err))]
        self.listener_oncomplete = [lambda nil: logging.debug("--- completed") ]
    def addOnNext(self,fn ) :
        self.listener_onnext.append(fn)
    def addOnError(self, fn  ) : 
        self.listener_onerror.append(fn)
    def addOnComplete(self,fn) :
        self.listener_oncomplete.append(fn) 
    
    def t_onnext(self) : 
        logging.debug("on next called")
        def on_next(value:T): 
            logging.debug("we are in on_next")
            for fn in self.listener_onnext :
                fn(value)
        return on_next
    def t_onerror(self) : 
        def on_error(err:Exception) : 
            for fn in self.listener_onerror : 
                fn(err) 
        return on_error 
    def t_oncomplete(self): 
        def on_complete() :
            for fn in self.listener_oncomplete : 
                fn() 
        return on_complete
print("\nCall Center Simulator")
from collections import deque 

class CallCenterSimulator:
    def __init__(self):
        self.incoming_calls = deque()  # Queue for incoming calls
        self.handled_calls = []  # Stack for reviewing last handled calls
        self.resolved_issues = []  # List for storing resolved issues
    
    # enqeue
    def new_call(self, call_id):
        print(f"New call received: {call_id}")
        self.incoming_calls.append(call_id)
    
    # deque
    def handle_call(self):
        if self.incoming_calls:
            call_id = self.incoming_calls.popleft() 
            print(f"Handling call: {call_id}")
            self.handled_calls.append(call_id)
            return call_id
        else:
            print("No incoming calls to handle.")
            return None
    
    #  peek
    def review_last_call(self):
        if self.handled_calls:
            last_call = self.handled_calls[-1]  
            print(f"Reviewing last handled call: {last_call}")
            return last_call
        else:
            print("No calls have been handled yet.")
            return None
    
    
    def resolve_call(self):
        last_call = self.review_last_call()
        if last_call:
            resolved_issue = f"Resolved call: {last_call}"
            self.resolved_issues.append(resolved_issue)  
            self.handled_calls.pop()  
            print(f"Call {last_call} resolved.")
    
  
    def show_resolved_issues(self):
        if self.resolved_issues:
            print("Resolved issues:")
            for issue in self.resolved_issues:
                print(issue)
        else:
            print("No issues have been resolved yet.")


call_center = CallCenterSimulator()


call_center.new_call("Call_1")
call_center.new_call("Call_2")
call_center.new_call("Call_3")


call_center.handle_call() 
call_center.resolve_call() 

call_center.handle_call()  
call_center.resolve_call() 


call_center.review_last_call() # Show all resolved issues


call_center.show_resolved_issues() # Show all resolved issues
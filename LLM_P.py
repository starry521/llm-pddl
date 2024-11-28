import argparse
from src import *

class LLM_P:
    def __init__(self, args):
        self.args = args
        self.domain = self.initialize_domain()
        self.planner = Planner()

    def initialize_domain(self):
        """Initialize the domain based on the argument"""
        domain_class = eval(self.args.domain.capitalize())
        return domain_class()

    def plan(self):
        """Execute the LLM planner"""
        print("[LLM_P] \033[34mInfo\033[0m: Start Planning!")
        method = {
            "llm_ic_pddl_planner": llm_ic_pddl_planner,
            "llm_pddl_planner": llm_pddl_planner,
            "llm_planner": llm_planner,
            "llm_stepbystep_planner": llm_stepbystep_planner,
            "llm_ic_planner": llm_ic_planner,
            "llm_tot_ic_planner": llm_tot_ic_planner,
        }[self.args.method]

        if self.args.print_prompts:
            print_all_prompts(self.planner)
        else:
            method(self.args, self.planner, self.domain)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="LLM-Planner")
    # DOMAIN is selected from [barman, blocksworld, floortile, grippers, storage, termes, tyreworld]
    parser.add_argument('--domain', type=str, choices=DOMAINS, default="barman")
    # METHOD is selected from [llm_ic_pddl_planner, llm_pddl_planner, llm_planner, llm_ic_planner]
    parser.add_argument('--method', type=str, choices=[
        "llm_ic_pddl_planner", "llm_pddl_planner", "llm_planner", 
        "llm_stepbystep_planner", "llm_ic_planner", "llm_tot_ic_planner"
    ], default="llm_ic_pddl_planner")
    parser.add_argument('--time-limit', type=int, default=200)
    # ptask.pddl(input task file)
    parser.add_argument('--task', type=int, default=0)
    parser.add_argument('--run', type=int, default=0)
    parser.add_argument('--print-prompts', action='store_true')
    args = parser.parse_args()

    # Initialize and execute the planner
    llm_planner = LLM_P(args)
    llm_planner.plan()
